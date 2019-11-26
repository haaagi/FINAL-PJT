<template>
    <div class="signup-form">
        <div v-if="isLoading" class="spinner-border" role="status">
            <span class="sr-only">Loading</span>
        </div>

        <form v-else class="signup-input" @submit.prevent="signup(credentials)">
            <div v-if="getErrors.length" class="error-list alert alert-danger">
                <p>아래의 오류를 해결해 주세요</p>
                <ul>
                    <li v-for="(error, idx) in getErrors" :key="idx">
                        {{ error }}
                    </li>
                </ul>
            </div>

            <div class="form-group">
                <label for="username">ID</label>
                <input v-model="userInput.username" type="text" class="form-control" id="username"
                    placeholder="아이디를 입력해주세요">
            </div>

            <div class="form-group">
                <label for="password">Password</label>
                <input v-model="userInput.password" type="password" class="form-control" id="password"
                    placeholder="비밀번호를 입력해주세요">
            </div>

            <div class="form-group">
                <label for="passwordConfirmation">PasswordConfirmation</label>
                <input v-model="userInput.passwordConfirmation" type="text" class="form-control" id="username"
                    placeholder="아이디를 입력해주세요">
            </div>

            <div class="form-group">
                <label for="age">Age</label>
                <input v-model="userInput.age" type="text" class="form-control" id="username"
                    placeholder="아이디를 입력해주세요">
            </div>

            <div class="form-group">
                <label for="gender">gender</label>
                <input v-model="userInput.gender" type="text" class="form-control" id="username"
                    placeholder="아이디를 입력해주세요">
            </div>
            
            <div class="form-group">
                <label for="kakao_id">카카오톡 ID</label>
                <input v-model="userInput.gender" type="text" class="form-control" id="username"
                    placeholder="아이디를 입력해주세요">
            </div>

            <button class="btn btn-primary">로그인</button>
        </form>
    </div>

</template>

<script>
    import {
        mapGetters,
        mapActions
    } from 'vuex';

    export default {
        name: 'SignupForm',
        data() {
            return {
                userInput: {
                    username: '',
                    password: '',
                    passwordConfirmation: '',
                    age: '',
                    gender: '',
                    kakao_id: '',

                }
            }
        },
        methods: {
            ...mapActions(['signup']),
        },
        computed: {
            ...mapGetters(['getErrors']),
        }

    }
</script>

<style>

</style>