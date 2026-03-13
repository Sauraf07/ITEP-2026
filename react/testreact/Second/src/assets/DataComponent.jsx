import { Component } from "react";
import Data from "./Data.js"

class DataComponent extends Component{
    constructor(){
        super();
        this.state = {
            productList: Data
        }
    }
    render(){
        console.log(this.state.productList)
        return <>
        <h1>Product Lists..</h1>
        <table border="1" width="100%">
            <tr>
                    <td>Name</td>
                    <td>Image</td>
                    <td>Price</td>
                    <td>Quantity</td>

            </tr>
            {this.state.productList.map((obj,index)=>{
                return <tr key={obj.id}>
                    <td>{obj.total}</td>
                    <td></td>

                </tr>
            })}
        </table>
        </>
    }

}
export default DataComponent