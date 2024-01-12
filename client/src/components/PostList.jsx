import React, { useEffect, useState } from "react";
import { CommentCreate, CommentList } from "./";
import axios from "axios";

const PostList = () => {
  const [posts, setPosts] = useState({});

  const fetchPosts = async () => {
    const response = await axios.get("http://posts.com/posts");
    setPosts(response.data);
  };

  useEffect(() => {
    fetchPosts();
  }, []);

  return (
    <>
      {Object.values(posts).map((post) => (
        <div
          key={post.id}
          className="flex flex-col items-start border border-black w-1/3 mt-5 p-4 gap-2"
        >
          <h2 className="text-3xl font-semibold">{post.title}</h2>
          <CommentList comments={post.comments} />
          <CommentCreate postId={post.id} />
        </div>
      ))}
    </>
  );
};

export default PostList;
