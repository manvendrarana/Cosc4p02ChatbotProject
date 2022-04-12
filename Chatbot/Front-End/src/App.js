import "./App.css";
import io from "socket.io-client";
import { useState } from "react";
import Chat from "./Components/Chat";


let socket = undefined;

function App() {
  const [username, setUsername] = useState("");
  const [showChat, setShowChat] = useState(false);

  const joinRoom = () => {
    if (username !== "") {
      setShowChat(true);
      socket = io.connect("http://localhost:3001");
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
              <Chat socket={socket} username={username}/>
          )}
      </div>
  );
}

export default App;
