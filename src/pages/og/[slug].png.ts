import type { APIRoute, GetStaticPaths } from "astro";
import satori from "satori";
import { Resvg } from "@resvg/resvg-js";
import { getPublishedPosts } from "../../lib/posts";

export const getStaticPaths: GetStaticPaths = async () => {
  const posts = await getPublishedPosts();
  return posts.map((post) => ({
    params: { slug: post.id },
    props: { title: post.data.title, description: post.data.description },
  }));
};

export const GET: APIRoute = async ({ props }) => {
  const { title, description } = props as {
    title: string;
    description?: string;
  };

  const svg = await satori(
    {
      type: "div",
      props: {
        style: {
          height: "100%",
          width: "100%",
          display: "flex",
          flexDirection: "column",
          justifyContent: "flex-end",
          padding: "60px",
          backgroundColor: "#fdfdfd",
          fontFamily: "sans-serif",
        },
        children: [
          {
            type: "div",
            props: {
              style: {
                display: "flex",
                flexDirection: "column",
                gap: "16px",
              },
              children: [
                {
                  type: "div",
                  props: {
                    style: {
                      fontSize: "52px",
                      fontWeight: 700,
                      color: "#1a1a1a",
                      lineHeight: 1.2,
                      letterSpacing: "-0.02em",
                    },
                    children: title,
                  },
                },
                ...(description
                  ? [
                      {
                        type: "div",
                        props: {
                          style: {
                            fontSize: "26px",
                            color: "#666",
                            lineHeight: 1.4,
                          },
                          children: description,
                        },
                      },
                    ]
                  : []),
                {
                  type: "div",
                  props: {
                    style: {
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "space-between",
                      marginTop: "24px",
                      paddingTop: "24px",
                      borderTop: "2px solid #e5e5e5",
                    },
                    children: [
                      {
                        type: "div",
                        props: {
                          style: {
                            fontSize: "24px",
                            fontWeight: 700,
                            color: "#1a1a1a",
                            letterSpacing: "-0.02em",
                          },
                          children: "abindran.com",
                        },
                      },
                      {
                        type: "div",
                        props: {
                          style: {
                            fontSize: "22px",
                            fontWeight: 700,
                            color: "#ffffff",
                            backgroundColor: "#2563eb",
                            padding: "10px 28px",
                            borderRadius: "8px",
                          },
                          children: "Read more \u2192",
                        },
                      },
                    ],
                  },
                },
              ],
            },
          },
        ],
      },
    },
    {
      width: 1200,
      height: 630,
      fonts: [
        {
          name: "sans-serif",
          data: await fetchFont("Inter", 400),
          weight: 400,
          style: "normal",
        },
        {
          name: "sans-serif",
          data: await fetchFont("Inter", 700),
          weight: 700,
          style: "normal",
        },
      ],
    }
  );

  const resvg = new Resvg(svg, {
    fitTo: { mode: "width", value: 1200 },
  });
  const png = resvg.render().asPng();

  return new Response(png, {
    headers: { "Content-Type": "image/png" },
  });
};

async function fetchFont(family: string, weight: number): Promise<ArrayBuffer> {
  const url = `https://fonts.googleapis.com/css2?family=${family}:wght@${weight}&display=swap`;
  const cssResponse = await fetch(url);
  const css = await cssResponse.text();
  const fontUrl = css.match(
    /src: url\((.+?)\) format\('(opentype|truetype|woff2?)'\)/
  )?.[1];
  if (!fontUrl) throw new Error(`Could not find font URL for ${family}@${weight}`);
  const fontResponse = await fetch(fontUrl);
  return fontResponse.arrayBuffer();
}
