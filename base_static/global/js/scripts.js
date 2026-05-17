(() => {
  const forms = document.querySelectorAll('.form-delete');

  for (const form of forms) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      const confirmed = confirm('Are you sure?');

      if (confirmed) {
        form.submit();
      }
    });
  }
})();

(() => {
  const buttonCloseMenu = document.querySelector('.button-close-menu');
  const buttonShowMenu = document.querySelector('.button-show-menu');
  const menuContainer = document.querySelector('.menu-container');

  const buttonShowMenuVisibleClass = 'button-show-menu-visible';
  const menuHiddenClass = 'menu-hidden';

  const closeMenu = () => {
    buttonShowMenu.classList.add(buttonShowMenuVisibleClass);
    menuContainer.classList.add(menuHiddenClass);
  };

  const showMenu = () => {
    buttonShowMenu.classList.remove(buttonShowMenuVisibleClass);
    menuContainer.classList.remove(menuHiddenClass);
  };

  if (buttonCloseMenu) {
    buttonCloseMenu.removeEventListener('click', closeMenu);
    buttonCloseMenu.addEventListener('click', closeMenu);
  }

  if (buttonShowMenu) {
    buttonShowMenu.removeEventListener('click', showMenu);
    buttonShowMenu.addEventListener('click', showMenu);
  }

  // Fecha o menu ao clicar em qualquer lugar da página que não seja uma postagem
  document.addEventListener('click', (e) => {
    if (!menuContainer || !buttonShowMenu) return;
    // só age se o menu estiver aberto
    if (menuContainer.classList.contains(menuHiddenClass)) return;

    const target = e.target;

    // não fecha se o clique for dentro do menu ou nos botões de abrir/fechar
    if (menuContainer.contains(target)) return;
    if (buttonShowMenu.contains(target)) return;
    if (buttonCloseMenu && buttonCloseMenu.contains(target)) return;

    // não fecha se o clique ocorrer dentro de uma postagem
    if (target.closest('.recipe, .recipe-list-item')) return;

    // caso contrário, fecha o menu
    closeMenu();
  });
})();

(() => {
  const authorsLogoutLinks = document.querySelectorAll('.authors-logout-link');
  const formLogout = document.querySelector('.form-logout');

  for (const link of authorsLogoutLinks) {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      formLogout.submit();
    });
  }
})();
