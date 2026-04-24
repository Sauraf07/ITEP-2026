import { useState } from "react";
import data from "../Data";
import Department from "./Department";

function Header() {
  const [departments] = useState(data.departments);
  const [Id, setId] = useState(null);

  return (
    <div className="container-fluid">
      <div className="bg-primary text-white text-center py-2">
        <h4>Departments</h4>
      </div>
      <div className="p-2">
        <button className="btn btn-success" onClick={() => {}}>
          Add Department
        </button>
      </div>
      <div className="px-3"> 
        {departments.map((d) => (
          <Department  key={d.id} dept={d} Id={Id} setId={setId} />  ))}
      </div>
    </div>
  );
}

export default Header;