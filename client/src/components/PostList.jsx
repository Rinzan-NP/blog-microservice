import React, { useEffect, useState } from "react";
import CommentList from "./CommentList";
import CommentCreate from "./CommentCreate";
import axios from "axios";

const PostList = () => {
  const [posts, setPosts] = useState([]);

  const fetchPosts = async () => {
    try {
      const response = await axios.get("http://posts.com/api/posts/");
      setPosts(response.data);
    } catch (error) {
      console.error("Error fetching posts:", error);
    }
  };

  useEffect(() => {
    fetchPosts();
  }, []);

  const renderRows = () => {
    const rows = [];
    for (let i = 0; i < posts.length; i += 3) {
      const rowPosts = posts.slice(i, i + 3);
      const row = (
        <div className="flex flex-row mb-5" key={i}>
          {rowPosts.map((post) => (
            <div
              key={post.id}
              className="flex flex-col items-start border border-black w-1/3 mx-2 p-4 space-y-2"
            >
              <h2 className="text-3xl font-semibold">{post.title}</h2>
              <CommentList comments={post.comments} />
              <CommentCreate postId={post.id} />
            </div>
          ))}
        </div>
      );
      rows.push(row);
    }
    return rows;
  };

  return <div className="w-full p-5">{renderRows()}</div>;
};

export default PostList;
