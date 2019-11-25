<template>
  <div class="home">
    <div>
      <ul>
        <li v-for="movie in movies" :key="movie.id">
          {{ movie.title }}
        </li>
      </ul>
    </div>


<MovieHome />

  </div>
</template>

<script>
// @ is an alias to /src
// import router from '../router';
const axios = require('axios'); 
import MovieHome from '../components/MovieHome';


export default {
  name: 'home',
  data () {
    return {
      movies: [],
    }
  },
  components: {
    MovieHome,
  },
  // methods: {
  //   addmovie() {
  //     axios.get('http://localhost:8000/api/movies/')
  //     .then(res=> {
  //       this.movie.push(res.data);
        
  //       console.log(res)
  //     })
  //   }
  // },
  created () {
    axios.get('http://localhost:8000/api/movies/')
      .then(res=> this.movies = res.data)
      .catch(err => console.error(err))
  }
}
</script>

