<template>

<div class="home">
<div class="scene scene--card">
  <div class="card">
    <div class="card__face card__face--front">front</div>
    <div class="card__face card__face--back">back</div>
  </div>
</div>
<p>Click card to flip.</p>

</div>


  <!-- <div class="home">
   <b-card-group>
<div v-for="movie in movies" :key="movie.id">
  <b-card
    :title="movie.title"
    :img-src="movie.poster_url"
    :img-alt="movie.title"
    img-top
    tag="article"
    style="max-width: 20rem;"
    class="mb-2"
    img-width="100"
  
  >

    <b-button href="#" variant="primary">Go somewhere</b-button>
  </b-card>

</div>
  </b-card-group>
</div> -->




    <!-- <div>
      <ul>
        <li v-for="movie in movies" :key="movie.id">
          <img :src="movie.poster_url" :alt="movie.title">
          <p>{{movie.title}}</p>
        </li>
      </ul>
    </div>

  </div> -->
</template>

<script>

// import router from '../router';
const axios = require('axios'); 
// import MovieHome from '../components/MovieHome';

// var card = document.querySelector('.card');
// card.addEventListener( 'click', function() {
//   card.classList.toggle('is-flipped');
// });

export default {
  name: 'home',
  data () {
    return {
      movies: [],
    }
  },
  components: {
  },
  created () {
    axios.get('http://localhost:8000/api/movies/')
      .then(res=> this.movies = res.data)
      .catch(err => console.error(err))
  }
}


</script>

<style>
body { font-family: sans-serif; }

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
}
</style>