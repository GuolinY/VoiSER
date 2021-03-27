<template>
  <v-container>
    <v-row>
      <v-col cols="3" v-for="(user, index) in users" :key="index">
        <User :userData="user" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import User from "./User.vue";

export default {
  name: "UserGrid",
  // props: {
  //   users: Array,
  // },
  components: {
    User,
  },
  data() {
    // Temporary list of users for debugging
    const numUsers = 100;
    const users = Array.from({ length: numUsers }, (_, i) => ({
      name: `User${i}`,
      isSpeaking: i % 2 == 0, //"random"
      emoticon: "😍",
    }));

    return {
      users,
    };
  },
};
</script>
