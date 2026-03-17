import { Component } from "react";
import Data from "./data";

class DataComponent extends Component {
  constructor() {
    super();
    this.state = {
      recipeList: Data
    };
  }

  render() {
    return (
      <>
        <h1 style={{ textAlign: "center", marginBottom: "30px" }}>
          Recipe List
        </h1>

        <div style={styles.container}>
          {this.state.recipeList.map((obj) => (
            <div key={obj.id} style={styles.card}>
              
              <img
                src={obj.image}
                alt={obj.name}
                style={styles.image}
              />

              <h3>{obj.name}</h3>

              <p>
                <strong>Difficulty:</strong> {obj.difficulty}
              </p>

              <p>
                <strong>Cook Time:</strong> {obj.cookTimeMinutes} minutes
              </p>
              <button><b>Make It Now !</b> </button>
            </div>
          ))}
        </div>
      </>
    );
  }
}

const styles = {
  
  container: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))",
    gap: "20px",
    padding: "20px",
    background:"navyblue"
  },

  card: {
    border: "1px solid #0987ed",
    borderRadius: "10px",
    padding: "15px",
    textAlign: "center",
    background: "#f0f408",
  },

  image: {
    width: "100%",
    height: "150px",
    objectFit: "cover",
    borderRadius: "8px",
    marginBottom: "10px"
  }
};

export default DataComponent;

/* this  application is made by react.js.
 it has a list of items based on how to cook recipies that is easy and simple.
  and easy to cook based on that it has given all the materials what is required to make this recipes items .
  it has multiple 
*/