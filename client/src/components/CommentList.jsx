import React, { useEffect, useState } from "react";
import axios from "axios";

const CommentList = (props) => {
  const { comments } = props;

  
  return (
    <div>
      <span>{comments.length} comment</span>
      <ul className="list-disc ml-10">
        {comments.map((comment,i) => (
          <li key={i}>{comment.comment}</li>
        ))}
      </ul>
    </div>
  );
};

export default CommentList;
