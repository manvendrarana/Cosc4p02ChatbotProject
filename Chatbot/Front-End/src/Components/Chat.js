import React, {useEffect, useState} from 'react';
import ScrollToBottom from 'react-scroll-to-bottom';
import {FaChevronCircleRight,} from 'react-icons/fa';
import {FaEraser} from 'react-icons/fa';
import {FaTwitter, FaFacebook, FaInstagram, FaYoutube, FaTiktok} from 'react-icons/fa';
import {FcInfo} from 'react-icons/fc';
import {saveAs} from 'file-saver';


function Chat({socket, username}) {
    const [currentMessage, setCurrentMessage] = useState("");
    const [messageList, setMessageList] = useState([]);
    const greetings = ["Hello, how may I assist you?", "Hi, what do you need help with?", "Hello, what questions do you have about the games?"];
    let chatbot_ready = true;

    const sendMessageAsBot = async (message) => {
        const messageData = {
            author: "Chatbot",
            title: message["title"],
            url: message["url"],
            message: message["answer"],
            time: new Date(Date.now()).getHours() + ":" + (new Date(Date.now()).getMinutes() < 10 ? '0' : '') + (new Date(Date.now()).getMinutes()),
        };
        setMessageList((list) => [...list, messageData]);
    }

    useEffect(() => {
        const greetingFinal = greetings[Math.floor(Math.random() * greetings.length)];
        sendMessageAsBot({title: "N/A", url: "N/A", answer: greetingFinal});
    }, []);

    const sendMessage = async () => {
        if (currentMessage !== "") {
            const messageData = {
                author: username,
                message: currentMessage,
                time: new Date(Date.now()).getHours() + ":" + //Added formating so it will show 9:03 for three minutes instead of 9:3
                    (new Date(Date.now()).getMinutes() < 10 ? '0' : '') + (new Date(Date.now()).getMinutes()),
            };
            if (socket.connected !== false) {
                chatbot_ready = false
                console.log(chatbot_ready)
                socket.emit("message", messageData, (message) => {
                    sendMessageAsBot(message)
                    chatbot_ready = true
                });
                setMessageList((list) => [...list, messageData]);
                setCurrentMessage("");
            } else {
                setMessageList((list) => [...list, messageData]);
                setCurrentMessage("");
                await sendMessageAsBot({
                    "title": "N/A",
                    "url": "N/A",
                    "answer": "Server is down, message was not sent."
                });
            }
        }
    };

    const saveList = async () => {
        let str = '#################################################\nNIAGRA CANADA GAMES 2022 CHAT BOT\nYou have Saved a Chat from the date of ' + new Date(Date.now()).getDate() + "/" + (new Date(Date.now()).getMonth() + 1) + "/" + new Date(Date.now()).getFullYear() + "\n#################################################\n\n";
        messageList.map(messageContent => {
            str += ["Message: " + messageContent.message + "\nFrom: " + messageContent.author + "\nTime: " + messageContent.time + "\n\n"];
        });
        const blob = new Blob([str], {type: "text/plain;charset=utf-8"});
        saveAs(blob, "SavedChatLog.txt");
    }

    const startNewChat = async () => {
        const greetingFinal = greetings[Math.floor(Math.random() * greetings.length)];
        setMessageList([]);
        await sendMessageAsBot(greetingFinal);
    }

    const clearInput = async () => {
        setCurrentMessage("");
    }

    return (<div className="chat-window" function={sendMessageAsBot}>
            <div className="chat-header">
                <ul className='header-list'>
                    <text className='chat-title'>
                        <text id='state'>
                            {
                                chatbot_ready ? "Waiting for user..." : "Chatbot is creating a response"
                            }
                        </text>
                    </text>
                    <a href='https://twitter.com/2022canadagames' className='social-button' target="_blank"
                       rel="noreferrer">
                        <FaTwitter/>
                    </a>
                    <a className='social-button' href='https://www.facebook.com/2022canadagames/' target="_blank"
                       rel="noreferrer">
                        <FaFacebook/>
                    </a>
                    <a className='social-button' href='https://www.instagram.com/2022canadagames' target="_blank"
                       rel="noreferrer">
                        <FaInstagram/>
                    </a>
                    <a className='social-button' href='https://www.youtube.com/channel/UCpWP6p7_J_aWuP8TpbTQJnAc'
                       target="_blank" rel="noreferrer">
                        <FaYoutube/>
                    </a>
                    <a className='social-button' href='https://www.tiktok.com/@niagara2022' target="_blank"
                       rel="noreferrer">
                        <FaTiktok/>
                    </a>
                </ul>
            </div>
            <div className="chat-body">
                <ScrollToBottom className="message-container">
                    {messageList.map((messageContent) => {
                        return (<div
                            className="message"
                            id={username === messageContent.author ? "you" : "other"}>
                            <div>
                                <div className="message-content">
                                    <text>{messageContent.message}</text>
                                </div>
                                <div className="message-meta">
                                    <text id="time">{messageContent.time}</text>
                                    <text id="author">{messageContent.author}</text>
                                    {messageContent.url!=="N/A" &&
                                        (<text>
                                            {username === messageContent.author ? "" :
                                                <a href={messageContent.url} title={messageContent.title} target="_blank"
                                                   rel="noreferrer" className='social-button'>
                                                    <FcInfo/>
                                                </a>
                                            }
                                        </text>)
                                    }

                                </div>
                            </div>
                        </div>);
                    })}
                </ScrollToBottom>
            </div>
            <div className="chat-footer">
                <button onClick={clearInput}><FaEraser/></button>
                <textarea type="text"
                          value={currentMessage}
                          placeholder={chatbot_ready ? "Type Inquire Here..." : "Chat-bot is responding"}
                          onChange={(event) => {
                              setCurrentMessage(event.target.value);
                          }}
                          onKeyPress={(event) => {
                              if (event.key === 'Enter') {
                                  event.preventDefault()
                              }
                              event.key === "Enter" && sendMessage();
                          }}
                          readOnly={!chatbot_ready}
                />
                <button onClick={sendMessage}><FaChevronCircleRight/></button>
            </div>
            <div className='new-chat'>
                <button onClick={saveList}>SAVE CHAT LOG</button>
                <button onClick={startNewChat}>CREATE A NEW CHAT</button>
            </div>
        </div>

    );
}

export default Chat;