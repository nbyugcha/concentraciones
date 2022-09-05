const { createApp } = Vue;

createApp({
  data() {
    return {
      resultadoConcentracion: '',
      data: {
        caudal: undefined,
        tiempoBacheo: undefined,
        volumenBiocida: undefined,
      },
    };
  },
  methods: {
    enviarConcentracion() {
      this.resultadoConcentracion = ''
      fetch("/concentracion", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(this.data),
      })
        .then((response) => response.json())
        .then((data) => {
          this.resultadoConcentracion = data.resultado
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
  },
}).mount("#app");
