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
  props: {
    users: Array,
  },
  components: {
    User,
  },
};
</script>
