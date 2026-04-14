import { getCollection } from "astro:content";

export async function getPublishedPosts() {
  const posts = await getCollection("posts");
  const now = new Date();
  now.setHours(0, 0, 0, 0);

  return posts.filter((post) => {
    const postDate = new Date(post.data.date);
    postDate.setHours(0, 0, 0, 0);
    return postDate <= now;
  });
}
