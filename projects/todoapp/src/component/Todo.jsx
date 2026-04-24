import { useState, useEffect } from 'react';
import { toast } from 'react-toastify';

const TodoApp = () => {
  const [todos, setTodos] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [filter, setFilter] = useState('all'); // all, active, completed

  // Load todos from localStorage when component mounts
  useEffect(() => {
    const savedTodos = localStorage.getItem('todos');
    if (savedTodos) {
      setTodos(JSON.parse(savedTodos));
    }
  }, []);

  // Save todos to localStorage whenever todos change
  useEffect(() => {
    localStorage.setItem('todos', JSON.stringify(todos));
  }, [todos]);

  // Add new todo
  const addTodo = (e) => {
    e.preventDefault();

    if (inputValue.trim() === '') {
      toast.error('Please enter a task!');
      return;
    }

    const newTodo = {
      id: Date.now(),
      text: inputValue.trim(),
      completed: false
    };

    setTodos([...todos, newTodo]);
    setInputValue('');
    toast.success('Task added successfully! ✅');
  };

  // Toggle complete status
  const toggleComplete = (id) => {
    setTodos(todos.map(todo =>
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ));
    
    const todo = todos.find(t => t.id === id);
    if (todo && !todo.completed) {
      toast.success('Task completed! 🎉');
    }
  };

  // Delete a todo
  const deleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id));
    toast.error('Task deleted');
  };

  // Clear all completed tasks
  const clearCompleted = () => {
    setTodos(todos.filter(todo => !todo.completed));
    toast.info('Completed tasks cleared');
  };

  // Filter todos based on current filter
  const filteredTodos = todos.filter(todo => {
    if (filter === 'active') return !todo.completed;
    if (filter === 'completed') return todo.completed;
    return true; // 'all'
  });

  const activeTodosCount = todos.filter(todo => !todo.completed).length;

  return (
    <div className="row justify-content-center">
      <div className="col-lg-8 col-md-10">

        {/* Add Todo Form */}
        <div className="card shadow mb-4">
          <div className="card-body">
            <h3 className="card-title text-center mb-4">Add New Task</h3>
            
            <form onSubmit={addTodo} className="d-flex gap-2">
              <input
                type="text"
                className="form-control form-control-lg"
                placeholder="What needs to be done?"
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
              />
              <button 
                type="submit"
                className="btn btn-success btn-lg px-4"
              >
                Add Task
              </button>
            </form>
          </div>
        </div>

        {/* Filters */}
        {todos.length > 0 && (
          <div className="d-flex justify-content-between align-items-center mb-3 px-2">
            <div>
              <span className="badge bg-primary fs-6">
                {activeTodosCount} active
              </span>
            </div>
            
            <div className="btn-group" role="group">
              <button 
                className={`btn btn-outline-primary ${filter === 'all' ? 'active' : ''}`}
                onClick={() => setFilter('all')}
              >
                All
              </button>
              <button 
                className={`btn btn-outline-primary ${filter === 'active' ? 'active' : ''}`}
                onClick={() => setFilter('active')}
              >
                Active
              </button>
              <button 
                className={`btn btn-outline-primary ${filter === 'completed' ? 'active' : ''}`}
                onClick={() => setFilter('completed')}
              >
                Completed
              </button>
            </div>

            {todos.some(todo => todo.completed) && (
              <button 
                className="btn btn-outline-danger btn-sm"
                onClick={clearCompleted}
              >
                Clear Completed
              </button>
            )}
          </div>
        )}

        {/* Todo List */}
        <div className="card shadow">
          <div className="card-header bg-light d-flex justify-content-between align-items-center">
            <h5 className="mb-0">Your Tasks ({filteredTodos.length})</h5>
          </div>
          
          <div className="card-body p-0">
            {filteredTodos.length === 0 ? (
              <div className="text-center py-5 text-muted">
                <h4>
                  {filter === 'completed' ? 'No completed tasks' : 
                   filter === 'active' ? 'No active tasks' : 'No tasks yet'}
                </h4>
                <p>Add a task above to get started</p>
              </div>
            ) : (
              <ul className="list-group list-group-flush">
                {filteredTodos.map((todo) => (
                  <li 
                    key={todo.id}
                    className="list-group-item d-flex justify-content-between align-items-center py-3"
                  >
                    <div className="d-flex align-items-center flex-grow-1">
                      <input 
                        type="checkbox"
                        className="form-check-input me-3"
                        checked={todo.completed}
                        onChange={() => toggleComplete(todo.id)}
                      />
                      <span 
                        className={todo.completed ? 'text-decoration-line-through text-muted' : ''}
                        style={{ fontSize: '1.1rem' }}
                      >
                        {todo.text}
                      </span>
                    </div>
                    
                    <button 
                      className="btn btn-sm btn-outline-danger"
                      onClick={() => deleteTodo(todo.id)}
                    >
                      Delete
                    </button>
                  </li>
                ))}
              </ul>
            )}
          </div>
        </div>

        {/* Footer Info */}
        {todos.length > 0 && (
          <div className="text-center mt-4 text-muted small">
            <p>Tasks are automatically saved in your browser</p>
          </div>
        )}

      </div>
    </div>
  );
};

export default TodoApp;