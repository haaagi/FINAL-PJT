<template>
  <div class="home">
    <navbar />
    <div>
      <ul>
        <li v-for="movie in movies" :key="movie.id">
          <img :src="movie.poster_url" :alt="movie.title">
          <p>{{movie.title}}</p>
        </li>
      </ul>
    </div>


  </div>
</template>

<script>

// import router from '../router';
const axios = require('axios'); 
// import MovieHome from '../components/MovieHome';
import navbar from '../components/navbar';

export default {
  name: 'home',
  data () {
    return {
      movies: [],
    }
  },
  components: {
    navbar,
  },
  created () {
    axios.get('http://localhost:8000/api/movies/')
      .then(res=> this.movies = res.data)
      .catch(err => console.error(err))
  }
}


</script>

