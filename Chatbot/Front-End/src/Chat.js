import React, { useEffect, useState } from 'react';
import ScrollToBottom from 'react-scroll-to-bottom';
import { FaChevronCircleRight } from 'react-icons/fa';
import setShowChat from './App.js';

function Chat({ socket, username, room }) {
  const [currentMessage, setCurrentMessage] = useState("");
  const [messageList, setMessageList] = useState([]);

  const sendMessage = async () => {
    if (currentMessage !== "") {
      const messageData = {
        room: room,
        author: username,
        message: currentMessage,
        time:
          new Date(Date.now()).getHours() +
          ":" +
          new Date(Date.now()).getMinutes(),
      };

      await socket.emit("send_message", messageData);
      setMessageList((list) => [...list, messageData]);
      setCurrentMessage("");
    }
  };


  useEffect(() => {
    socket.on("receive_message", (data) => {
      setMessageList((list) => [...list, data]);
    });
  }, [socket]);


  const saveList = async () => {{
      messageList.map((messageContent) => {
        console.log(messageContent.message,". From:", messageContent.author, "@:", messageContent.time);
      })
    }
  }

  const startNewChat = async () =>{
    setMessageList([]);
  }

  const sendMessageBot = async () => {
    const messageData = {
      room: room,
      author: "Chatbot",
      message: "Peakey Blinders",
      time:
        new Date(Date.now()).getHours() +
        ":" +
        new Date(Date.now()).getMinutes(),
    };

    await socket.emit("send_message", messageData);
    setMessageList((list) => [...list, messageData]);
    //THis will clear the chats 
    //setMessageList([]);
  }

  return (
    <div className="chat-window">
      <div className="chat-header"><p>Live Chat</p></div>
      <div className="chat-body">
        <ScrollToBottom className="message-container">
          {messageList.map((messageContent) => {
            return (
              <div
                className="message"
                id={username === messageContent.author ? "you" : "other"}>
                <div>
                  <div className="message-content">
                    <p>{messageContent.message}</p>
                  </div>
                  <div className="message-meta">
                    <p id="time">{messageContent.time}</p>
                    <p id="author">{messageContent.author}</p>
                  </div>
                </div>
              </div>
            );
          })}
        </ScrollToBottom>
      </div>
      <div className="chat-footer">
        <input
          type="text"
          value={currentMessage}
          placeholder="Type Inquire Here..."
          onChange={(event) => {
            setCurrentMessage(event.target.value);
          }}
          onKeyPress={(event) => {
            event.key === "Enter" && sendMessage();
          }}
        />
        <button onClick={sendMessage}><FaChevronCircleRight /></button>
      </div>
      <div className='new-chat'>
        <button onClick={saveList}>SAVE CHAT LOG</button>
        <button onClick={startNewChat}>CREATE A NEW CHAT</button>
      </div>
    </div>
  );
}

export default Chat;
