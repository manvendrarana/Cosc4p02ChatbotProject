import "./ChatLogin.css";
import {useState} from "react";
import Chat from "./Chat";

function ChatLogin({connected_to_server, socket, connect}) {
    const [username, setUsername] = useState("");
    const [showChat, setShowChat] = useState(false);

    const joinRoom = () => {
        if (username !== "") {
            setShowChat(true);
            if (!connected_to_server) {
                connect();
            }
        }
    };

    return (
        <div className="App">
            {!showChat ? (
                <div className="joinChatContainer">
                    <input
                        type="text"
                        placeholder="John..."
                        onChange={(event) => {
                            setUsername(event.target.value);
                        }}
                    />
                    <button onClick={joinRoom}>START CHAT</button>
                </div>
            ) : (
                <Chat connected_to_server={connected_to_server} socket={socket} username={username}/>
            )}
        </div>
    );
}

export default ChatLogin;
