import React, {useState} from 'react';


function LoginForm({Login, error, checking_credentials}) {
    const [details, setDetails] = useState({name: "", password: ""})
    const onSubmit = e => {
        e.preventDefault();
        Login(details);
    }
    console.log("is disabled?", details.username === "" || details.password === "" || checking_credentials)
    return (
        <form onSubmit={onSubmit}>
            <div className="form">
                <h1 className="form-heading">Login</h1>
                {error !== "" ? <h3 className="form-error">{error}</h3> : ""}
                <div className="input-container">
                    <input className="input-field" type="text" name="name" id="name" placeholder="name"
                           onChange={e => setDetails({...details, username: e.target.value})} value={details.username}/>
                </div>
                <div className="input-container">
                    <input className="input-field" type="password" name="password" id="password" placeholder="password"
                           onChange={e => setDetails({...details, password: e.target.value})}
                           value={details.password}/>
                </div>
                <input className={checking_credentials ? "active input-submit" : "input-submit"} type="submit"
                       value={checking_credentials ? "Checking Credentials" : (details.username === "" || details.password === "") ? "Enter Credentials" : "Login"}
                       disabled={details.username === "" || details.password === "" || checking_credentials}/>
            </div>
        </form>
    );
}

export default LoginForm;