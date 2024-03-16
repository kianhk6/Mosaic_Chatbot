import React from "react";
import styles from "./ChatBubble.module.css";

const ChatBubble = ({ text, isUser, avatar }) => (
  <div
    className={`${styles.bubble} ${
      isUser ? styles.userMessage : styles.botMessage
    }`}
  >
    {!isUser && avatar}
    <span className={styles.messageText}>{text}</span>
  </div>
);

export default ChatBubble;
