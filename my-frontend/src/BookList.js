// src/components/BookList.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function BookList() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/books/')
      .then(res => setBooks(res.data))
      .catch(err => console.log(err));
  }, []);

  return (
    <div>
      <h2>Books:</h2>
      <ul>
        {books.map(book => <li key={book.id}>{book.title}</li>)}
      </ul>
    </div>
  );
}

export default BookList;