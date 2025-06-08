import { Button } from "@/components/ui/button";
import Icon from "@/components/ui/icon";

const Header = () => {
  return (
    <header className="bg-white border-b border-gray-200 sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <div className="flex items-center">
            <div className="flex items-center gap-2">
              <div className="w-8 h-8 bg-gradient-to-r from-purple-500 to-blue-500 rounded-lg flex items-center justify-center">
                <Icon name="CreditCard" size={20} className="text-white" />
              </div>
              <span className="text-xl font-bold text-gray-900 font-montserrat">
                PayFlow
              </span>
            </div>
          </div>

          <nav className="hidden md:flex items-center space-x-8">
            <a
              href="#services"
              className="text-gray-600 hover:text-purple-600 transition-colors"
            >
              Услуги
            </a>
            <a
              href="#pricing"
              className="text-gray-600 hover:text-purple-600 transition-colors"
            >
              Тарифы
            </a>
            <a
              href="#about"
              className="text-gray-600 hover:text-purple-600 transition-colors"
            >
              О нас
            </a>
            <a
              href="#contact"
              className="text-gray-600 hover:text-purple-600 transition-colors"
            >
              Контакты
            </a>
          </nav>

          <div className="flex items-center gap-3">
            <Button
              variant="ghost"
              className="text-gray-600 hover:text-purple-600"
            >
              Войти
            </Button>
            <Button className="bg-purple-600 hover:bg-purple-700 text-white">
              Начать работу
            </Button>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
