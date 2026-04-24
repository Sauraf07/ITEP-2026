import Employee from "./Employee";

function Department({ dept, openId, setOpenId }) {
  return (
    <div className="mb-4">
      <p>{dept.id}</p>
      <h2>{dept.name}</h2>
      <p>{dept.employees.length} items</p>    
      <div className="btn-group">
        <button className="btn btn-outline-dark" onClick={() => setOpenId(openId === dept.id ? null : dept.id)} >   View Employees
        </button>
        <button className="btn btn-outline-dark" onClick={() => {}}>
          Add Employee
        </button>
  <button className="btn btn-outline-dark" onClick={() => {}}>
          Edit
        </button>
        <button className="btn btn-outline-dark" onClick={() => {}}>
          Delete
        </button>
      </div>
      {openId === dept.id && dept.employees.map((emp) => (
          <Employee key={emp.id} emp={emp} />
        ))}
    </div>
  );
}

export default Department;