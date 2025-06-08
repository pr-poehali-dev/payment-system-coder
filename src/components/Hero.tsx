import { Button } from "@/components/ui/button";
import Icon from "@/components/ui/icon";

const Hero = () => {
  return (
    <section className="bg-gradient-to-br from-purple-50 to-blue-50 py-20 lg:py-32">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          <div className="text-center lg:text-left">
            <h1 className="text-4xl lg:text-6xl font-bold text-gray-900 mb-6 font-montserrat">
              Платежи нового
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-purple-600 to-blue-600">
                {" "}
                поколения
              </span>
            </h1>
            <p className="text-xl text-gray-600 mb-8 leading-relaxed">
              Принимайте платежи от клиентов по всему миру с минимальными
              комиссиями и максимальной безопасностью. Интеграция за 5 минут.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start">
              <Button className="bg-purple-600 hover:bg-purple-700 text-white px-8 py-3 text-lg">
                <Icon name="Play" size={20} className="mr-2" />
                Начать работу
              </Button>
              <Button
                variant="outline"
                className="border-purple-600 text-purple-600 hover:bg-purple-50 px-8 py-3 text-lg"
              >
                <Icon name="BookOpen" size={20} className="mr-2" />
                Документация
              </Button>
            </div>

            <div className="flex items-center gap-6 mt-12 justify-center lg:justify-start">
              <div className="text-center">
                <div className="text-2xl font-bold text-gray-900">99.9%</div>
                <div className="text-sm text-gray-600">Uptime</div>
              </div>
              <div className="text-center">
                <div className="text-2xl font-bold text-gray-900">0.5%</div>
                <div className="text-sm text-gray-600">Комиссия</div>
              </div>
              <div className="text-center">
                <div className="text-2xl font-bold text-gray-900">24/7</div>
                <div className="text-sm text-gray-600">Поддержка</div>
              </div>
            </div>
          </div>

          <div className="relative">
            <div className="bg-white rounded-2xl shadow-2xl p-8">
              <div className="bg-gradient-to-r from-purple-500 to-blue-500 rounded-lg p-6 text-white mb-6">
                <div className="flex items-center justify-between mb-4">
                  <Icon name="CreditCard" size={24} />
                  <span className="text-sm opacity-80">PayFlow</span>
                </div>
                <div className="text-2xl font-bold mb-2">₽ 125,430</div>
                <div className="text-sm opacity-80">Доступно к выводу</div>
              </div>

              <div className="space-y-4">
                <div className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                  <div className="flex items-center gap-3">
                    <div className="w-8 h-8 bg-green-100 rounded-full flex items-center justify-center">
                      <Icon
                        name="ArrowDownLeft"
                        size={16}
                        className="text-green-600"
                      />
                    </div>
                    <div>
                      <div className="font-medium text-gray-900">
                        Входящий платеж
                      </div>
                      <div className="text-sm text-gray-600">Order #12345</div>
                    </div>
                  </div>
                  <div className="text-green-600 font-medium">+₽5,200</div>
                </div>

                <div className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                  <div className="flex items-center gap-3">
                    <div className="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center">
                      <Icon
                        name="ArrowUpRight"
                        size={16}
                        className="text-blue-600"
                      />
                    </div>
                    <div>
                      <div className="font-medium text-gray-900">Перевод</div>
                      <div className="text-sm text-gray-600">
                        На банковскую карту
                      </div>
                    </div>
                  </div>
                  <div className="text-gray-600 font-medium">-₽2,100</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
