import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './index.css';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

function App() {
  const [activeTab, setActiveTab] = useState('generate');
  const [url, setUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [quizData, setQuizData] = useState(null);
  const [history, setHistory] = useState([]);
  const [selectedQuiz, setSelectedQuiz] = useState(null);
  const [quizMode, setQuizMode] = useState(false);
  const [modalQuizMode, setModalQuizMode] = useState(false);
  const [userAnswers, setUserAnswers] = useState({});
  const [modalUserAnswers, setModalUserAnswers] = useState({});
  const [quizSubmitted, setQuizSubmitted] = useState(false);
  const [modalQuizSubmitted, setModalQuizSubmitted] = useState(false);
  const [score, setScore] = useState(null);
  const [modalScore, setModalScore] = useState(null);

  // Check backend connection on mount
  useEffect(() => {
    checkBackendConnection();
  }, []);

  // Fetch history on mount and when tab changes
  useEffect(() => {
    if (activeTab === 'history') {
      fetchHistory();
    }
  }, [activeTab]);

  const checkBackendConnection = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/api/health`, { timeout: 3000 });
      if (response.data.status === 'healthy') {
        console.log('✅ Backend connection successful');
        // Clear any previous connection errors
        if (error && error.includes('Cannot connect to backend')) {
          setError(null);
        }
      }
    } catch (err) {
      console.error('❌ Backend connection failed:', err.message);
      // Only show error if user tries to interact, not on initial load
      // Error will be shown when user tries to generate quiz
    }
  };

  const fetchHistory = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/api/quiz/history`);
      setHistory(response.data);
    } catch (err) {
      setError('Failed to fetch quiz history');
      console.error(err);
    }
  };

  const handleGenerateQuiz = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setQuizData(null);
    setQuizMode(false);
    setUserAnswers({});
    setQuizSubmitted(false);
    setScore(null);

    try {
      // First check if backend is available
      try {
        await axios.get(`${API_BASE_URL}/api/health`, { timeout: 2000 });
      } catch (healthErr) {
        setError(`Cannot connect to backend at ${API_BASE_URL}. Please ensure the backend server is running on port 8000.`);
        setLoading(false);
        return;
      }

      const response = await axios.post(`${API_BASE_URL}/api/quiz/generate`, {
        url: url
      });
      setQuizData(response.data);
      setUrl(''); // Clear input after successful generation
      // Enable quiz mode by default so users can immediately start answering
      setQuizMode(true);
      setUserAnswers({});
      setQuizSubmitted(false);
      setScore(null);
    } catch (err) {
      // Show more detailed error message
      if (err.code === 'ECONNREFUSED' || err.message.includes('Network Error')) {
        setError(`Cannot connect to backend at ${API_BASE_URL}. Please ensure the backend server is running on port 8000.`);
      } else {
        const errorMessage = err.response?.data?.detail || 
                            err.response?.data?.message || 
                            err.message || 
                            'Failed to generate quiz. Please check the URL and try again.';
        setError(errorMessage);
      }
      console.error('Quiz generation error:', err);
      console.error('Error details:', err.response?.data);
    } finally {
      setLoading(false);
    }
  };

  const handleViewDetails = async (articleId) => {
    try {
      const response = await axios.get(`${API_BASE_URL}/api/quiz/${articleId}`);
      setSelectedQuiz(response.data);
    } catch (err) {
      setError('Failed to fetch quiz details');
      console.error(err);
    }
  };

  const handleCloseModal = () => {
    setSelectedQuiz(null);
    setModalQuizMode(false);
    setModalUserAnswers({});
    setModalQuizSubmitted(false);
    setModalScore(null);
  };

  const handleAnswerSelect = (questionIndex, selectedAnswer, isModal = false) => {
    // Only allow selection if in quiz mode and not submitted
    const currentQuizMode = isModal ? modalQuizMode : quizMode;
    const currentSubmitted = isModal ? modalQuizSubmitted : quizSubmitted;
    
    if (!currentQuizMode || currentSubmitted) {
      return; // Don't allow selection if not in quiz mode or already submitted
    }
    
    if (isModal) {
      setModalUserAnswers({
        ...modalUserAnswers,
        [questionIndex]: selectedAnswer
      });
    } else {
      setUserAnswers({
        ...userAnswers,
        [questionIndex]: selectedAnswer
      });
    }
  };

  const handleSubmitQuiz = (isModal = false) => {
    const quiz = isModal ? selectedQuiz : quizData;
    if (!quiz) return;
    
    const answers = isModal ? modalUserAnswers : userAnswers;
    let correctCount = 0;
    
    quiz.quiz.forEach((question, index) => {
      if (answers[index] === question.answer) {
        correctCount++;
      }
    });
    
    const totalQuestions = quiz.quiz.length;
    const percentage = Math.round((correctCount / totalQuestions) * 100);
    
    const scoreData = {
      correct: correctCount,
      total: totalQuestions,
      percentage: percentage
    };
    
    if (isModal) {
      setModalScore(scoreData);
      setModalQuizSubmitted(true);
    } else {
      setScore(scoreData);
      setQuizSubmitted(true);
    }
  };

  const renderQuiz = (quiz, isModal = false) => {
    if (!quiz) return null;

    const currentQuizMode = isModal ? modalQuizMode : quizMode;
    const currentSubmitted = isModal ? modalQuizSubmitted : quizSubmitted;
    const currentAnswers = isModal ? modalUserAnswers : userAnswers;
    const currentScore = isModal ? modalScore : score;

    return (
      <div className="quiz-container">
        <div className="article-info">
          <h2>{quiz.title}</h2>
          <p><strong>URL:</strong> <a href={quiz.url} target="_blank" rel="noopener noreferrer">{quiz.url}</a></p>
          <p><strong>Summary:</strong> {quiz.summary}</p>
          
          {quiz.sections && quiz.sections.length > 0 && (
            <div>
              <strong>Sections:</strong>
              <div className="sections-list">
                {quiz.sections.map((section, idx) => (
                  <span key={idx} className="section-tag">{section}</span>
                ))}
              </div>
            </div>
          )}

          {quiz.key_entities && (
            <div className="entities">
              {quiz.key_entities.people && quiz.key_entities.people.length > 0 && (
                <div>
                  <strong>People:</strong>
                  {quiz.key_entities.people.map((person, idx) => (
                    <span key={idx} className="entity-tag">{person}</span>
                  ))}
                </div>
              )}
              {quiz.key_entities.organizations && quiz.key_entities.organizations.length > 0 && (
                <div>
                  <strong>Organizations:</strong>
                  {quiz.key_entities.organizations.map((org, idx) => (
                    <span key={idx} className="entity-tag">{org}</span>
                  ))}
                </div>
              )}
              {quiz.key_entities.locations && quiz.key_entities.locations.length > 0 && (
                <div>
                  <strong>Locations:</strong>
                  {quiz.key_entities.locations.map((loc, idx) => (
                    <span key={idx} className="entity-tag">{loc}</span>
                  ))}
                </div>
              )}
            </div>
          )}
        </div>

        <div className="quiz-mode-controls">
          {!currentQuizMode && !currentSubmitted && (
            <button
              className="btn btn-primary"
              onClick={() => {
                if (isModal) {
                  setModalQuizMode(true);
                  setModalUserAnswers({});
                  setModalQuizSubmitted(false);
                  setModalScore(null);
                } else {
                  setQuizMode(true);
                  setUserAnswers({});
                  setQuizSubmitted(false);
                  setScore(null);
                }
              }}
            >
              🎯 Start Quiz Mode
            </button>
          )}
          {currentQuizMode && !currentSubmitted && (
            <>
              <button 
                className="btn btn-secondary" 
                onClick={() => {
                  if (isModal) {
                    setModalQuizMode(false);
                    setModalUserAnswers({});
                    setModalQuizSubmitted(false);
                    setModalScore(null);
                  } else {
                    setQuizMode(false);
                    setUserAnswers({});
                    setQuizSubmitted(false);
                    setScore(null);
                  }
                }}
              >
                Exit Quiz Mode
              </button>
              <button 
                className="btn btn-submit" 
                onClick={() => handleSubmitQuiz(isModal)}
              >
                ✅ Submit Quiz ({Object.keys(currentAnswers).length}/{quiz.quiz.length} answered)
              </button>
            </>
          )}
          {currentSubmitted && (
            <>
              <div className="score-summary">
                <h3>Quiz Results</h3>
                <p>You answered {Object.keys(currentAnswers).length} out of {quiz.quiz.length} questions</p>
              </div>
              <button
                className="btn btn-primary"
                onClick={() => {
                  if (isModal) {
                    setModalQuizMode(true);
                    setModalUserAnswers({});
                    setModalQuizSubmitted(false);
                    setModalScore(null);
                  } else {
                    setQuizMode(true);
                    setUserAnswers({});
                    setQuizSubmitted(false);
                    setScore(null);
                  }
                }}
              >
                🔄 Retake Quiz
              </button>
            </>
          )}
        </div>

        {currentScore && (
          <div className="score-display">
            Score: {currentScore.correct}/{currentScore.total} ({currentScore.percentage}%)
          </div>
        )}

        <div className="quiz-questions">
          {quiz.quiz && quiz.quiz.map((question, index) => {
            const userAnswer = currentAnswers[index];
            const isCorrect = userAnswer === question.answer;
            // Only show answers AFTER quiz is submitted, not before
            const showAnswer = currentSubmitted;

            return (
              <div key={index} className="question-card">
                <div className="question-header">
                  <span className="question-text">
                    {index + 1}. {question.question}
                  </span>
                  <span className={`difficulty-badge difficulty-${question.difficulty}`}>
                    {question.difficulty}
                  </span>
                </div>
                <div className="options">
                  {question.options.map((option, optIndex) => {
                    let optionClass = 'option';
                    let isDisabled = false;
                    
                    // Only allow selection if quiz mode is active and not submitted
                    if (currentQuizMode && !currentSubmitted) {
                      // User can select answers
                      if (option === userAnswer) {
                        optionClass += ' selected';
                      }
                    } else if (currentSubmitted) {
                      // Quiz submitted - show correct/incorrect
                      isDisabled = true;
                      if (option === question.answer) {
                        optionClass += ' correct';
                      } else if (option === userAnswer && option !== question.answer) {
                        optionClass += ' incorrect';
                      }
                    } else {
                      // Not in quiz mode - show all options normally (no selection)
                      isDisabled = true;
                    }

                    return (
                      <div
                        key={optIndex}
                        className={optionClass}
                        onClick={() => handleAnswerSelect(index, option, isModal)}
                        style={{
                          cursor: (currentQuizMode && !currentSubmitted) ? 'pointer' : 'default',
                          opacity: isDisabled ? 0.7 : 1,
                          userSelect: 'none'
                        }}
                      >
                        <span className="option-label">{String.fromCharCode(65 + optIndex)}.</span>
                        <span className="option-text">{option}</span>
                        {currentSubmitted && option === question.answer && (
                          <span className="correct-indicator"> ✓ Correct Answer</span>
                        )}
                        {currentSubmitted && option === userAnswer && option !== question.answer && (
                          <span className="incorrect-indicator"> ✗ Your Answer (Wrong)</span>
                        )}
                        {currentSubmitted && userAnswer && option === userAnswer && option === question.answer && (
                          <span className="correct-indicator"> ✓ Your Answer (Correct!)</span>
                        )}
                      </div>
                    );
                  })}
                </div>
                {currentSubmitted && (
                  <div className={`explanation ${isCorrect ? 'explanation-correct' : 'explanation-incorrect'}`}>
                    <strong>{isCorrect ? '✓ Correct!' : '✗ Incorrect'}</strong>
                    <br />
                    <strong>Explanation:</strong> {question.explanation}
                  </div>
                )}
              </div>
            );
          })}
        </div>

        {quiz.related_topics && quiz.related_topics.length > 0 && (
          <div className="related-topics">
            <h3>Related Topics</h3>
            <div className="topics-list">
              {quiz.related_topics.map((topic, idx) => (
                <span key={idx} className="topic-tag">{topic}</span>
              ))}
            </div>
          </div>
        )}
      </div>
    );
  };

  return (
    <div className="container">
      <div className="header">
        <h1>📚 Wiki Quiz App</h1>
        <p>Generate quizzes from Wikipedia articles using AI</p>
      </div>

      <div className="tabs">
        <button
          className={`tab ${activeTab === 'generate' ? 'active' : ''}`}
          onClick={() => setActiveTab('generate')}
        >
          Generate Quiz
        </button>
        <button
          className={`tab ${activeTab === 'history' ? 'active' : ''}`}
          onClick={() => setActiveTab('history')}
        >
          Past Quizzes
        </button>
      </div>

      <div className="tab-content">
        {activeTab === 'generate' && (
          <div>
            <form onSubmit={handleGenerateQuiz}>
              <div className="form-group">
                <label htmlFor="url">Wikipedia Article URL</label>
                <input
                  type="url"
                  id="url"
                  value={url}
                  onChange={(e) => setUrl(e.target.value)}
                  placeholder="https://en.wikipedia.org/wiki/Alan_Turing"
                  required
                  disabled={loading}
                />
              </div>
              <button type="submit" className="btn" disabled={loading}>
                {loading ? 'Generating Quiz...' : 'Generate Quiz'}
              </button>
            </form>

            {error && <div className="error">{error}</div>}

            {loading && <div className="loading">⏳ Generating quiz from Wikipedia article...</div>}

            {quizData && renderQuiz(quizData)}
          </div>
        )}

        {activeTab === 'history' && (
          <div>
            <h2>Quiz History - All Processed Wikipedia URLs</h2>
            {history.length === 0 ? (
              <p>No quizzes generated yet. Go to "Generate Quiz" tab to create one!</p>
            ) : (
              <div>
                <div className="history-summary">
                  <p><strong>Total Articles:</strong> {history.length}</p>
                </div>
                <table className="history-table">
                  <thead>
                    <tr>
                      <th>ID</th>
                      <th>Title</th>
                      <th>Wikipedia URL</th>
                      <th>Created At</th>
                      <th>Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                    {history.map((article) => (
                      <tr key={article.id}>
                        <td>{article.id}</td>
                        <td><strong>{article.title}</strong></td>
                        <td>
                          <a href={article.url} target="_blank" rel="noopener noreferrer" className="url-link">
                            {article.url}
                          </a>
                        </td>
                        <td>{new Date(article.created_at).toLocaleString()}</td>
                        <td>
                          <button
                            className="btn"
                            onClick={() => handleViewDetails(article.id)}
                          >
                            View Quiz
                          </button>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>
        )}
      </div>

      {selectedQuiz && (
        <div className="modal-overlay" onClick={handleCloseModal}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <button className="modal-close" onClick={handleCloseModal}>×</button>
            {renderQuiz(selectedQuiz, true)}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
