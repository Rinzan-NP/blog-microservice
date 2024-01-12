import axios from "axios";
import React, { useState } from "react";

const PostCreate = () => {
  const [title, setTitle] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    await axios.post("http://posts.com/posts/create", {
      title,
    });

    setTitle("");
  };
  return (
    <>
      <div className="w-1/3">
        <h1 className="text-4xl font-bold">Create Post</h1>
        <form onSubmit={handleSubmit}>
          <div className="flex flex-col">
            <label htmlFor="" className="text-2xl font-normal my-3">
              Title
            </label>
            <input
              type="text"
              className="px-2 py-2 border border-black outline-none"
              placeholder="Enter your title here..."
              value={title}
              onChange={(e) => setTitle(e.target.value)}
            />
          </div>
          <button
            type="submit"
            className="btn px-4 py-2 border mt-4 border-black rounded-full "
          >
            Submit
          </button>
        </form>
      </div>
    </>
  );
};

export default PostCreate;
