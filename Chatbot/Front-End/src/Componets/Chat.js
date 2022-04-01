import React, { useEffect, useState } from 'react';
import ScrollToBottom from 'react-scroll-to-bottom';
import { FaChevronCircleRight, } from 'react-icons/fa';
import { FaEraser } from 'react-icons/fa';
import { FaTwitter, FaFacebook, FaInstagram, FaYoutube, FaTiktok } from 'react-icons/fa';
import { saveAs } from 'file-saver';


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
          //Added formating so it will show 9:03 for three minutes instead of 9:3
          (new Date(Date.now()).getMinutes() < 10 ? '0' : '') + (new Date(Date.now()).getMinutes()),
      };

      await socket.emit("send_message", messageData, (message) => { sendMessageBot(message) });
      setMessageList((list) => [...list, messageData]);
      setCurrentMessage("");
      
      var element = document.getElementById("state");
      element.innerHTML = "Chatbot is creating a response...";
    }
  };

  // not req
  useEffect(() => {
    socket.on("receive_message", (data) => {
      console.log("got something", data)
      setMessageList((list) => [...list, data]);
    });
  }, [socket]);

  const saveList = async () => {
    let str = '#################################################\nNIAGRA CANADA GAMES 2022 CHAT BOT\nYou have Saved a Chat from the date of ' + new Date(Date.now()).getDate() + "/" + (new Date(Date.now()).getMonth() + 1) + "/" + new Date(Date.now()).getFullYear() + "\n#################################################\n\n";
    messageList.map(messageContent => {
      str += ["Message: " + messageContent.message + "\nFrom: " + messageContent.author + "\nTime: " + messageContent.time + "\n\n"];
    });
    var blob = new Blob([str], { type: "text/plain;charset=utf-8" });
    saveAs(blob, "SavedChatLog.txt");
  }

  const startNewChat = async () => {
    var greetingFinal = greetings[Math.floor(Math.random() * greetings.length)];
    setMessageList([]);
    sendMessageBot(greetingFinal);
    var element = document.getElementById("state");
    element.innerHTML = "Waiting for user...";
  }

  const sendMessageBot = async (message) => {
    const messageData = {
      room: room,
      author: "Chatbot",
      message: message,
      time:
        new Date(Date.now()).getHours() +
        ":" +
        (new Date(Date.now()).getMinutes() < 10 ? '0' : '') + (new Date(Date.now()).getMinutes()),
    };

    //await socket.emit("send_message", messageData); not needed
    setMessageList((list) => [...list, messageData]);
  }

  useEffect(() => {
    var greetingFinal = greetings[Math.floor(Math.random() * greetings.length)];
    sendMessageBot(greetingFinal);
  }, []);

  return (
    <div className="chat-window" function={sendMessageBot}>
      <div className="chat-header">
        <ul className='header-list'>
          <text className='chat-title'>
            <text id='state'>Waiting for user...</text>
          </text>
          <a href='https://twitter.com/2022canadagames' className='social-button'>
            <FaTwitter />
          </a>
          <a className='social-button' href='https://www.facebook.com/2022canadagames/'>
            <FaFacebook />
          </a>
          <a className='social-button' href='https://www.instagram.com/2022canadagames'>
            <FaInstagram />
          </a>
          <a className='social-button' href='https://www.youtube.com/channel/UCpWP6p7_J_aWuP8TpbTQJnAc'>
            <FaYoutube />
          </a>
          <a className='social-button' href='https://www.tiktok.com/@niagara2022'>
            <FaTiktok/>
          </a>
        </ul>
      </div>
      <div className="chat-body">
        <ScrollToBottom className="message-container">
          {messageList.map((messageContent) => {
            return (
              <div
                className="message"
                id={username === messageContent.author ? "you" : "other"}>
                <div>
                  <div className="message-content">
                    <text>{messageContent.message}</text>
                  </div>
                  <div className="message-meta">
                    <text id="time">{messageContent.time}</text>
                    <text id="author">{messageContent.author}</text>
                  </div>
                </div>
              </div>
            );
          })}
        </ScrollToBottom>
      </div>
      <div className="chat-footer">
        <button onClick={clearInput}><FaEraser /></button>
        <textarea type="text"
          value={currentMessage}
          placeholder="Type Inquire Here..."
          onChange={(event) => {
            setCurrentMessage(event.target.value);
          }}
          onKeyPress={(event) => {
            if (event.key === 'Enter') {
              event.preventDefault()
            }
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