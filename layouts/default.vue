<template>
  <v-app dark>
    <v-app-bar :clipped-left="clipped" fixed app>
      <v-btn icon @click.stop="clipped = !clipped">
        <v-icon>mdi-camera</v-icon>
      </v-btn>
      <v-toolbar-title>{{ title }}</v-toolbar-title>
      
    </v-app-bar>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
    <v-footer :absolute="!fixed" app>
      <span>&copy; {{ new Date().getFullYear() }} Hugo y Martin UACH </span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: "DefaultLayout",
  data() {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: "AI Food & Recipes App",
    };
  },
};
</script>
