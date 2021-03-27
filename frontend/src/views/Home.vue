<template>
  <div class="home">
    <UserGrid :users="users" />
  </div>
</template>

<script>
import UserGrid from "@/components/UserGrid";

export default {
  name: "Home",
  components: {
    UserGrid,
  },
  data() {
    // Temporary list of users for debugging
    const numUsers = 300;
    const users = Array.from({ length: numUsers }, (_, i) => ({
      name: `User${i}`,
      isSpeaking: i % 3 == 0, //"random"
      emotion: "😍",
    }));

    return {
      users,
    };
  },
};
</script>
