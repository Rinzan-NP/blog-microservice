import React, { useEffect, useState } from "react";
import axios from "axios";

const CommentList = (props) => {
  const { postId } = props;

  const [comments, setComments] = useState([]);
  const fetchComments = async () => {
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/api/comments/${postId}`
      );

      setComments(response.data);
    } catch (error) {
      console.error("Error fetching posts:", error);
    }
  };
  useEffect(() => {
    fetchComments();
  }, []);

  return (
    <div>
      <span>{comments.length} comment</span>
      <ul className="list-disc ml-10">
        {comments.map((comment) => (
          <li key={comment.id}>{comment.comment}</li>
        ))}
      </ul>
    </div>
  );
};

export default CommentList;
