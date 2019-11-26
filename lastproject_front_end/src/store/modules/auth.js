const axios = require('axios');
import router from '../../router';

const state = {
    token: null,
    errors: [],
    loading: false,
};


const getters = {
    isLoggedIn: (state) => {
        if (state.token === null) {
            return false;
        } else {
            return true;
        }
    },
    getErrors: state =>state.errors,
    isLoading: state =>state.loading,
};

const mutations = {
    setLoading: (state, flag) => state.loading = flag,
    setToken: (state, token) => {
        state.token = token;
        sessionStorage.setItem('jwt', token);
    },
    pushError: (state, error) => state.errors.push(error),
    clearErrors: state => state.errors = [],
};

const actions = {
    logout: ({ commit }) => {
        commit('setToken', null);
        sessionStorage.removeItem('jwt');
        router.push('/login');
    },

    pushError: ({ commit },error) => {
        commit('pushError', error)
    },

    login: ({ commit, getters }, credentials) => {
        if (getters.isLoggedIn) {
            router.push('/')
        } else { // 로그인이 안됐다면
            commit('clearErrors');
            commit('setLoading',true);
        if (!credentials.username) {
            commit('pushError', 'username can not be empty');
            commit('setLoading',false);
        }
        if (!credentials.password < 8) {
            commit('pushError','password must be at least 8');
            commit('setLoading',false);
        }
        else {
            axios.post('http://localhost:8000/api-token-auth/', credentials)
                .then(token => {
                    commit('setToken',token.data.token);
                    commit('setLoading',false);
                    router.push('/');
                })
                .catch(err => {
                    if (!err.response) { // no reponse
                        commit('pushError', 'Network Error..')
                    } else if (err.response.status === 400) {
                        commit('pushError', 'Invalid username or password');
                    } else if (err.response.status === 500) {
                        commit('pushError', 'Internal Server error. Please try again later');
                    } else {
                        commit('pushError', 'Some error occured');
                    }
                    commit('setLoading', false);
                })
            }

        }
    },
    signup: ({ commit, getters, dispatch }, {username, password, age, gender, kakao_id}) => {
        if (getters.isLoggedIn) {
            router.push('/');
        } else {
            axios.post('http://localhost:8000/signup', userInput)
                .then(res => {
                    if (res.status === 200) {
                        router.push('/')
                    } else {
                        router.push('login/')
                    }}
                )
                .catch(err => {
                    commit('pushError', err.response)
                })
        }
    }
};

export default {
    state, getters, mutations, actions
}