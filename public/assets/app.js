const navToggle=document.getElementById('navToggle');
const navMenu=document.getElementById('navMenu');
navToggle&&navToggle.addEventListener('click',()=>navMenu.classList.toggle('show'));
navMenu.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>navMenu.classList.remove('show')));

const form=document.getElementById('leadForm');
const msg=document.getElementById('formMsg');
form&&form.addEventListener('submit',async(e)=>{
  e.preventDefault();
  const fd=new FormData(form);
  const data={
    nombre:fd.get('nombre'),
    email:fd.get('email'),
    telefono:fd.get('telefono')||'',
    interes:fd.get('interes')||'',
    mensaje:fd.get('mensaje')||''
  };
  if(!data.nombre||!data.email){ msg.textContent='Por favor completa nombre y correo electrónico.'; return; }
  msg.textContent='Enviando...';
  try{
    const res=await fetch('api/leads', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(data)});
    const json=await res.json();
    if(json.success){ msg.textContent='¡Gracias! Tu solicitud ha sido registrada.'; form.reset(); }
    else msg.textContent=json.error||'Error al enviar.';
  }catch(err){ msg.textContent='Error de conexión. Intenta nuevamente.'; }
});
