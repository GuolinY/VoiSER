<template>
  <v-container>
    <v-row>
      <v-col cols="3" v-for="(user, index) in users" :key="index">
        <User :name="user.name" />
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
    const numUsers = 1;
    const users = Array.from({ length: numUsers }, (_, i) => ({
      name: `User${i}`,
    }));

    return {
      users,
    };
  },
};
</script>

<style lang="scss" scoped></style>
