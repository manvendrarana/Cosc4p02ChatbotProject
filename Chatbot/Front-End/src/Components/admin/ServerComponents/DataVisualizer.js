import React from 'react';

function DataVisualizer({connected_to_server, sid, socket, showError, data, setData}) {
    return (
        <div className="data-container">
            <button className="request-data" onClick={
                ()=>{
                    if(socket!==undefined){
                        socket.emit("view_scraped_documents", sid, (result)=>{
                            console.log(result)
                            if(result["result"]==="success"){
                                setData(Object.values(JSON.parse(result["response"].data)));
                            }else{
                                showError(result["response"])
                            }
                        })
                    }
                    else {
                        showError("Session lost please logout.")
                    }
                }
            }>Request Data</button>
            <div className="tables-container">
                {data.map((details) =>
                    <div className="table-container">
                        <div className="table-info-header">
                            <div className="url">
                                {details["url"]}
                            </div>
                            <div className="title">
                                {details["title"]}
                            </div>
                            <div className="section_title">
                                {details["section_title"]}
                            </div>
                        </div>
                        <table>
                            {
                                <tr>
                                    {
                                        details["columns"].map((values) =>
                                            <th>
                                                {values}
                                            </th>
                                        )
                                    }
                                </tr>
                            }
                            {
                                details["values"].map((row)=>
                                    <tr>
                                        {
                                            row.map((value) =>
                                                <td>
                                                    {value}
                                                </td>
                                            )
                                        }
                                    </tr>
                                )
                            }
                        </table>
                    </div>
                )}
            </div>
        </div>)
}

export default DataVisualizer;