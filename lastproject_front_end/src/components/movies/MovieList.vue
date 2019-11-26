<template>
    <div>
        <h1>MovieList</h1>
        <ul>
            <li v-for="movie in movies" :key="movie.id">
                <img :src="movie.poster_url" :alt="movie.title">
            </li>
        </ul>  
    </div>
</template>


<script>
export default {
    name: 'MovieList',
    data() {
        return {

        }
    },
    props: {
        Movies: Array,
    }
}
</script>

<style>
    
</style>