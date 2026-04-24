function Employee(props) {
  return (
    <div className="ms-4">
      Name:{props.emp.name} , Role: {props.emp.role}
    </div>      
  );
}

export default Employee;