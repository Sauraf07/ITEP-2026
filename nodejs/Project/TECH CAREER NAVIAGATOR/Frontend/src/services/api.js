import axios from 'axios';

const API_URL = 'http://localhost:3000/api';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add JWT token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const authAPI = {
  register: (data) => api.post('/auth/register', data),
  login: (data) => api.post('/auth/login', data),
};

export const profileAPI = {
  create: (data) => api.post('/profile/create', data),
  get: (userId) => api.get(`/profile/${userId}`),
};

export const subjectAPI = {
  getImportantList: () => api.get('/subjects/important-list'),
  add: (data) => api.post('/subjects/add', data),
  getAll: (userId) => api.get(`/subjects/${userId}`),
  markImportant: (subjectId) => api.put(`/subjects/${subjectId}/mark-important`),
  filterImportant: (data) => api.post('/subjects/filter-important', data),
};

export const careerAPI = {
  getPaths: () => api.get('/career/paths'),
  select: (data) => api.post('/career/select', data),
  getUser: (userId) => api.get(`/career/user/${userId}`),
};

export const roadmapAPI = {
  getByCareer: (careerField) => api.get(`/seed/careers/${encodeURIComponent(careerField)}/roadmap`),
  generate: (data) => api.post('/roadmap/generate', data),
  get: (userId) => api.get(`/roadmap/${userId}`),
};

export const taskAPI = {
  generate: (data) => api.post('/tasks/generate', data),
  getAll: (userId) => api.get(`/tasks/${userId}`),
  complete: (data) => api.post('/tasks/complete', data),
  getProgress: (userId) => api.get(`/tasks/progress/${userId}`),
};

export const seedAPI = {
  seedAll: () => api.post('/seed/seed'),
  getImportantSubjects: () => api.get('/seed/subjects/important'),
  getAllCareers: () => api.get('/seed/careers/all'),
  getCareerRoadmap: (careerField) => api.get(`/seed/careers/${careerField}/roadmap`),
};

export default api;