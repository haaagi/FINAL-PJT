<template>
    <div>

        <b-card-group deck>
            <div>
                <select v-model="genreNum">
                    <option :value="0">전체보기</option>
                </select>
            </div>
            <div class="row">
                <SelectedMovieList v-for="movie in movies" :key="movie.id" :movie="movie" />
            </div>
            <!-- <div v-for="movie in movies" :key="movie.id" class="col-3 my-3">
 
    <b-card title="Title" :img-src="movie.poster_url" :img-alt="movie.title" img-top>
      <b-card-text>
        This is a wider card with supporting text below as a natural lead-in to additional content.
        This content is a little bit longer.
      </b-card-text>
    </b-card> -->

    </b-card-group>



    <!-- <ul>
            <li v-for="movie in movies" :key="movie.id">
                <img :src="movie.poster_url" :alt="movie.title">
                {{ movie.title }}
            </li>
        </ul>   -->
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
            genreNum: 0,

        }
    },
    props: {
        movies: Array,
    }
}
</script>

<style>

</style>