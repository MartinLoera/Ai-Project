<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <v-card v-if="isLoading == false && isResponse == false">
        <v-card-title class="headline">
          Para empezar sube una foto donde salgan todos tus ingredientes, ten en
          cuenta la cantidad de luz en la sala.
        </v-card-title>
        <v-file-input
          v-model="image"
          label="Image input"
          accept="image/png, image/jpeg, image/bmp"
        ></v-file-input>
        <v-card-actions>
          <v-spacer />
          <v-btn color="primary" @click="sendImage"> Enviar </v-btn>
        </v-card-actions>
      </v-card>
      <v-card v-else-if="isLoading == true && isResponse == false">
        <div class="text-center">
          <v-progress-circular
            indeterminate
            color="primary"
          ></v-progress-circular>
        </div>
      </v-card>
      <v-card v-else>
        <div v-for="item in response" :key="item">
          
          <v-card>
            <v-btn color="success" @click="isResponse = false">Regresar</v-btn>
            <v-card-title primary-title>
              Nombre del Platillo: {{item[1]}} 
            </v-card-title>
            <v-card-title secondary-title>
              Ingredientes 
            </v-card-title>
            <v-card-text>
              {{item[2]}}
            </v-card-text>
            <v-card-title secondary-title>
              Instrucciones 
            </v-card-title>
            <v-card-text>
              {{item[3]}}
            </v-card-text>
          </v-card>
        </div>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
const FormData =  require("form-data");
import axios from "axios";

export default {
  name: "IndexPage",
  data() {
    return {
      image: null,
      isLoading: false,
      isResponse: false,
      response: null
    };
  },
  methods: {
    async sendImage() {
      this.isLoading = true
      if (this.image == null) {
        alert("Imagen vacia");
      } else {
        this.isLoading = true;
        const form =  new FormData();
        form.append("image", this.image);

        const response = await axios.post("http://35.193.135.203", form, {
          headers: {
            ... form.getHeaders
          }
        }).then(response => {
          this.response = response.data
        });
        this.isLoading = false
        this.isResponse = true
        
      }
    },
  },
};
</script>
