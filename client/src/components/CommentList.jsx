import React from "react";

const CommentList = ({ comments }) => {
    let content;

    return (
        <div>
            <span>{comments.length} comment</span>
            <ul className="list-disc ml-10">
                {comments.map((comment) => (
                    <li key={comment.id}>
                        {comment.status === "approved"
                            ? comment.content
                            : comment.status === "pending"
                            ? "This comment is being moderated"
                            : "This comment is rejected"}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default CommentList;
