<template>
<div class="modal fade" tabindex="-1" role="dialog" :id="`movie-${movie.id}`">

  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">

        <h5 class="modal-title">{{ movie.title }}</h5>
        
        <button @click="likeMovie(movie.id)"><i class="heart icon"></i></button>
        <button><i class="heart outline icon"></i></button>

        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">

        <img class="movie--poster my-3" :src="movie.poster_url" :alt="movie.name">
        <div>
        </div>
        <hr>
        <p>{{ movie.description }}</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>


</template>

<script>

const HOST = process.env.VUE_APP_SERVER_HOST;
const axios = require('axios'); 

  export default {
    name: 'MovieListItemModal',
    props: {
      movie: Object,
    },
    data () {
      return {
        // clickedMovie: 0,
      }
    },

    methods: {
      // clickLike(movie) {
      //   this.clickedMovie = movie;
      // },
      likeMovie (movie_id) {
            const hash = sessionStorage.getItem('jwt');
            const options = {
            headers: {
                Authorization:'JWT ' + hash
            }
        }
            axios.post(HOST + 'api/movielike/'+ movie_id + '/', options)            .then(res=> console.log(res))
            .then(res=> console.log(res))
            .catch(err => console.error(err))
            
        }

    },
    

  }
</script>

<style>

</style>