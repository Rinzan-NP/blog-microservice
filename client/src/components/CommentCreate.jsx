import axios from "axios";
import React, { useState } from "react";

const CommentCreate = (props) => {
  const { postId } = props;
  const [content, setContent] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
  
    axios.post(`http://127.0.0.1:8000/api/comments/${postId}`, {
      post_id: postId,
      comment: content,
    });

    setContent("");
  };

  return (
    <>
      <form onSubmit={handleSubmit}>
        <div className="flex flex-col w-full mb-2">
          <label htmlFor="">New Comment</label>
          <input
            className="px-2 py-1 mt-2 border w-full border-black outline-none"
            type="text"
            placeholder="Enter a comment.."
            value={content}
            onChange={(e) => setContent(e.target.value)}
          />
        </div>
        <button
          type="submit"
          className="btn px-4 py-1 border border-black rounded-md "
        >
          submit
        </button>
      </form>
    </>
  );
};

export default CommentCreate;
