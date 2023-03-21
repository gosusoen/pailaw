import React, { useState, useEffect } from 'react';
import axios from 'axios';

function testforapis() {
  const [data, setData] = useState([]);

  interface Product {
    id: number;
    name: string;
    price: number;
  }
  
useEffect(() => {
  fetch('/api/products/')
    .then(response => response.json())
    .then((_data: Product[]) => {
      setData(_data);
      console.log(data);
    });
}, []);

  useEffect(() => {
    axios.get('https://example.com/api/data')
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  return (
    <div>
    {data.map((item: any) => (
      <div key={item.id}>
        <h2>{item.title}</h2>
        <p>{item.body}</p>
      </div>
    ))}
  </div>
  );
}

export default testforapis;