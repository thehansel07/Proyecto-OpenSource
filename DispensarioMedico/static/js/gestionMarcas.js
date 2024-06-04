(function (){

    const btnEliminacion = document.querySelectorAll('.btnEliminacion');
       btnEliminacion.forEach(btn=>{
          btn.addEventListener('click', (e)=>{
          const confirmacion = confirm('Estas seguro que desea eliminar este registro?');
        if (!confirmacion){
            e.preventDefault();
        }
    });
});
})();