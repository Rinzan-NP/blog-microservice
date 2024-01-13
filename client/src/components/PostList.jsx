import React, { useEffect, useState } from "react";
import  CommentList from "./CommentList";
import CommentCreate from "./CommentCreate";
import axios from "axios";

const PostList = () => {
    const [posts, setPosts] = useState([]);
  
    const fetchPosts = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8001/api/posts/");
        setPosts(response.data);
      } catch (error) {
        console.error("Error fetching posts:", error);
      }
    };
  
    useEffect(() => {
      fetchPosts();
    }, []);
  
    return (
      <>
        {posts.map((post) => (
          <div
            key={post.id}
            className="flex flex-col items-start border border-black w-1/3 mt-5 p-4 gap-2"
          >
            <h2 className="text-3xl font-semibold">{post.title}</h2>
            <CommentList postId={post.id} />
            <CommentCreate postId={post.id} />
          </div>
        ))}
      </>
    );
  };
  
  export default PostList;
  