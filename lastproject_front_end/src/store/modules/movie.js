// const axios = require('axios');
import router from '../../router';


const state = {
    movieOne: '',
};


const getters = {
    getmovieOne: state => state.movieOne
};

const mutations = {
    setmovieOne: (state, one) => state.movieOne = one
};

const actions = {
    selectMovie: ({ commit, getters }) => {
        const hash = sessionStorage.getItem('jwt');
        const options = {
          headers: {
            Authorization: 'JWT ' + hash
          }
        }
        axios.get(HOST + 'api/movie_detail/' + this.movie.id + '/', options)
          .then(res => console.log(res))
          .catch(err => console.error(err))

    }
    
}
export default {
    state, getters, mutations, actions
}
