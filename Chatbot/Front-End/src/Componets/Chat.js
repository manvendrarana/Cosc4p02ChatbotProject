import React, { useEffect, useState } from 'react';
import ScrollToBottom from 'react-scroll-to-bottom';
import { FaChevronCircleRight, } from 'react-icons/fa';
import { FaEraser } from 'react-icons/fa';


function Chat({ socket, username, room }) {
  const [currentMessage, setCurrentMessage] = useState("");
  const [messageList, setMessageList] = useState([]);
  const greetings = ["Hello, how may I assist you?", "Hi, what do you need help with?", "Hello, what questions do you have about the games?"];


  const clearInput = async () => {
    setCurrentMessage("");
  }

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


  const saveList = async () => {
    messageList.map((messageContent) => {
      console.log(messageContent.message, " From:", messageContent.author, "@:", messageContent.time);
    });
  }

  const startNewChat = async () => {
    var greetingFinal = greetings[Math.floor(Math.random()*greetings.length)];
    setMessageList([]);
    sendMessageBot(greetingFinal);
  }

  const sendMessageBot = async (message) => {
    const messageData = {
      room: room,
      author: "Chatbot",
      message: message,
      time:
        new Date(Date.now()).getHours() +
        ":" +
        new Date(Date.now()).getMinutes(),
    };

    await socket.emit("send_message", messageData);
    setMessageList((list) => [...list, messageData]);
  }

  useEffect(() => {
    var greetingFinal = greetings[Math.floor(Math.random()*greetings.length)];
    sendMessageBot(greetingFinal);
  }, []);
  
  return (
    <div className="chat-window" function = {sendMessageBot}>
      <div className="chat-header"><text className='chat-title'>Live Chat/Location for Ai Status</text></div>
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
        <button onClick={clearInput}><FaEraser /></button>
        <input type="text"
          value={currentMessage}
          placeholder="Type Inquire Here..."
          onChange={(event) => {
            setCurrentMessage(event.target.value);
          }}
          onKeyPress={(event) => {
            event.key === "Enter" && sendMessage();
          }} />
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
