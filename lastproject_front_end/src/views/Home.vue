<template>
  <div class="home">
    <MovieList :movies="movies" />
  </div>
</template>

<script>

// import router from '../router';
const axios = require('axios'); 
// import MovieHome from '../components/MovieHome';
import MovieList from'../components/movies/MovieList';

export default {
  name: 'home',
  components: {
    MovieList,
  },
  data () {
    return {
      movies: [],
    }
  },
  created () {
    axios.get('http://localhost:8000/api/movies/')
      .then(res=> this.movies = res.data)
      .catch(err => console.error(err))
  }
}


</script>

<style>
<<<<<<< HEAD

=======
/* body { font-family: sans-serif; }

.scene {
  width: 200px;
  height: 260px;
  border: 1px solid #CCC;
  margin: 40px 0;
  perspective: 600px;
}

.card {
  position: relative;
  width: 100%;
  height: 100%;
  cursor: pointer;
  transform-style: preserve-3d;
  transform-origin: center right;
  transition: transform 1s;
}

.card.is-flipped {
  transform: translateX(-100%) rotateY(-180deg);
}

.card__face {
  position: absolute;
  width: 100%;
  height: 100%;
  line-height: 260px;
  color: white;
  text-align: center;
  font-weight: bold;
  font-size: 40px;
  backface-visibility: hidden;
}

.card__face--front {
  background: red;
}

.card__face--back {
  background: blue;
  transform: rotateY(180deg);
} */
>>>>>>> 9eb14928196fedc11e13fd6be993742a7bcdcd11
</style>