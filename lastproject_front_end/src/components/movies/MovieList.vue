<template>
  <div>
    
<div>
  <b-card title="Card Title" no-body>
    <b-card-header header-tag="nav">
      <b-nav card-header pills v-model="genreType">
        <b-nav-item active v-for="genre in genreList" :key="genre" :value="genre">{{ genre }}</b-nav-item>
        <b-nav-item>Inactive</b-nav-item>
        <b-nav-item disabled>Disabled</b-nav-item>
      </b-nav>
    </b-card-header>

    <b-card-body class="text-center">
      <b-card-text>
              <SelectedMovieList v-for="movie in filterMovies" :key="movie.id" :movie="movie">
        {{ movie }}
      </SelectedMovieList>
      </b-card-text>

    </b-card-body>
  </b-card>
</div>

     <!-- <div>
      <select v-model="genreType">
        <option v-for="genre in genreList" :key="genre" :value="genre">{{ genre }}</option>
      </select>
    </div> 

    <div class="row">
      <SelectedMovieList v-for="movie in filterMovies" :key="movie.id" :movie="movie">
        {{ movie }}
      </SelectedMovieList>
    </div>   -->
  </div> 
</template>


<script>
  import SelectedMovieList from './SelectedMovieList';

  export default {
    name: 'MovieList',
    components: {
      // MovieModal,
      SelectedMovieList,
    },
    data() {
      return {
        genreType: '전체보기',
        genreList: ['전체보기', '드라마', '액션', '범죄', '스릴러', '코미디', '공포(호러)', '멜로/로맨스', '미스터리', '애니메이션', '사극', 'SF']

      }
    },
    props: {
      movies: Array,
    },
    computed: {
      filterMovies() {

        if (this.genreType === '전체보기') {
          return this.movies
        } 
        else {
            return this.movies.filter(movie => movie.genre1 === this.genreType || movie.genre3 === this.genreType)
        }
      }
    },
  }
</script>

<style>
  select {
    display: block;
    width: 50% !important;
    margin: 2rem auto !important;
  }
</style>