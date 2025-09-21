import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class MetaFinanceAnalyzer:
    def __init__(self, platform_name):
        self.platform = platform_name
        self.colors = ['#1877F2', '#25D366', '#E4405F', '#F9A602', '#6A0572', 
                      '#AB83A1', '#5CAB7D', '#2A9D8F', '#E76F51', '#264653']
        
        self.start_year = 2010
        self.end_year = 2025
        
        # Configuration spécifique à chaque plateforme
        self.config = self._get_platform_config()
        
    def _get_platform_config(self):
        """Retourne la configuration spécifique pour chaque plateforme Meta"""
        configs = {
            "Facebook": {
                "users_base": 2000000000,
                "revenue_base": 85,
                "type": "social_media",
                "specialites": ["advertising", "marketplace", "gaming", "vr"]
            },
            "WhatsApp": {
                "users_base": 2000000000,
                "revenue_base": 5,
                "type": "messaging",
                "specialites": ["messaging", "business_api", "payments"]
            },
            "Instagram": {
                "users_base": 1500000000,
                "revenue_base": 45,
                "type": "visual_social",
                "specialites": ["advertising", "influencers", "shopping", "reels"]
            },
            # Configuration par défaut
            "default": {
                "users_base": 1000000000,
                "revenue_base": 30,
                "type": "social_media",
                "specialites": ["advertising", "user_data", "engagement"]
            }
        }
        
        return configs.get(self.platform, configs["default"])
    
    def generate_financial_data(self):
        """Génère des données financières pour la plateforme"""
        print(f"📊 Génération des données financières pour {self.platform}...")
        
        # Créer une base de données annuelle
        dates = pd.date_range(start=f'{self.start_year}-01-01', 
                             end=f'{self.end_year}-12-31', freq='Y')
        
        data = {'Annee': [date.year for date in dates]}
        
        # Données utilisateurs
        data['Utilisateurs_Actifs'] = self._simulate_active_users(dates)
        data['Utilisateurs_Quotidiens'] = self._simulate_daily_users(dates)
        
        # Revenus
        data['Revenus_Totaux'] = self._simulate_total_revenue(dates)
        data['Revenus_Publicite'] = self._simulate_ad_revenue(dates)
        data['Revenus_Autres'] = self._simulate_other_revenue(dates)
        
        # Dépenses
        data['Depenses_Totales'] = self._simulate_total_expenses(dates)
        data['Infrastructure'] = self._simulate_infrastructure_costs(dates)
        data['R_D'] = self._simulate_randd_costs(dates)
        data['Marketing'] = self._simulate_marketing_costs(dates)
        data['Personnel'] = self._simulate_staff_costs(dates)
        
        # Indicateurs financiers
        data['Profit_Net'] = self._simulate_net_profit(dates)
        data['Marge_Profit'] = self._simulate_profit_margin(dates)
        data['Cout_Acquisition_Utilisateur'] = self._simulate_cac(dates)
        data['Vie_Utilisateur'] = self._simulate_lifetime_value(dates)
        
        # Investissements par domaine
        data['Investissement_IA'] = self._simulate_ai_investment(dates)
        data['Investissement_VR'] = self._simulate_vr_investment(dates)
        data['Investissement_Securite'] = self._simulate_security_investment(dates)
        data['Investissement_Croissance'] = self._simulate_growth_investment(dates)
        data['Investissement_Contenu'] = self._simulate_content_investment(dates)
        
        df = pd.DataFrame(data)
        
        # Ajouter des tendances spécifiques à la plateforme
        self._add_platform_trends(df)
        
        return df
    
    def _simulate_active_users(self, dates):
        """Simule le nombre d'utilisateurs actifs"""
        base_users = self.config["users_base"]
        
        users = []
        for i, date in enumerate(dates):
            # Croissance différente selon la plateforme
            if self.platform == "Facebook":
                if date.year < 2018:
                    growth_rate = 0.12
                else:
                    growth_rate = 0.05  # Ralentissement après 2018
            elif self.platform == "Instagram":
                if date.year < 2020:
                    growth_rate = 0.25
                else:
                    growth_rate = 0.15
            elif self.platform == "WhatsApp":
                growth_rate = 0.10
            else:
                growth_rate = 0.08
                
            growth = 1 + growth_rate * i
            users.append(base_users * growth)
        
        return users
    
    def _simulate_daily_users(self, dates):
        """Simule le nombre d'utilisateurs quotidiens"""
        base_daily = self.config["users_base"] * 0.65  # 65% des utilisateurs actifs sont quotidiens
        
        daily_users = []
        for i, date in enumerate(dates):
            growth = 1 + 0.07 * i
            daily_users.append(base_daily * growth)
        
        return daily_users
    
    def _simulate_total_revenue(self, dates):
        """Simule les revenus totaux"""
        base_revenue = self.config["revenue_base"] * 1000  # Conversion en millions
        
        revenue = []
        for i, date in enumerate(dates):
            # Croissance variable selon la plateforme
            if self.platform == "Facebook":
                growth_rate = 0.25
            elif self.platform == "Instagram":
                growth_rate = 0.35
            elif self.platform == "WhatsApp":
                growth_rate = 0.40  # Croissance plus forte car part de plus petite base
            else:
                growth_rate = 0.20
                
            growth = 1 + growth_rate * i
            noise = np.random.normal(1, 0.10)
            revenue.append(base_revenue * growth * noise)
        
        return revenue
    
    def _simulate_ad_revenue(self, dates):
        """Simule les revenus publicitaires"""
        base_ad_revenue = self.config["revenue_base"] * 1000 * 0.98  # 98% des revenus viennent de la pub
        
        ad_revenue = []
        for i, date in enumerate(dates):
            growth = 1 + 0.22 * i
            noise = np.random.normal(1, 0.12)
            ad_revenue.append(base_ad_revenue * growth * noise)
        
        return ad_revenue
    
    def _simulate_other_revenue(self, dates):
        """Simule les autres revenus"""
        base_other = self.config["revenue_base"] * 1000 * 0.02  # 2% des revenus viennent d'autres sources
        
        other_revenue = []
        for i, date in enumerate(dates):
            growth = 1 + 0.30 * i  # Croissance plus forte pour les revenus non-publicitaires
            noise = np.random.normal(1, 0.15)
            other_revenue.append(base_other * growth * noise)
        
        return other_revenue
    
    def _simulate_total_expenses(self, dates):
        """Simule les dépenses totales"""
        base_expenses = self.config["revenue_base"] * 1000 * 0.65  # Dépenses à 65% des revenus
        
        expenses = []
        for i, date in enumerate(dates):
            growth = 1 + 0.20 * i
            noise = np.random.normal(1, 0.08)
            expenses.append(base_expenses * growth * noise)
        
        return expenses
    
    def _simulate_infrastructure_costs(self, dates):
        """Simule les coûts d'infrastructure"""
        base_infra = self.config["revenue_base"] * 1000 * 0.20  # 20% des revenus pour l'infrastructure
        
        infra_costs = []
        for i, date in enumerate(dates):
            growth = 1 + 0.15 * i
            noise = np.random.normal(1, 0.07)
            infra_costs.append(base_infra * growth * noise)
        
        return infra_costs
    
    def _simulate_randd_costs(self, dates):
        """Simule les coûts de R&D"""
        base_randd = self.config["revenue_base"] * 1000 * 0.15  # 15% des revenus pour la R&D
        
        randd_costs = []
        for i, date in enumerate(dates):
            growth = 1 + 0.18 * i
            noise = np.random.normal(1, 0.09)
            randd_costs.append(base_randd * growth * noise)
        
        return randd_costs
    
    def _simulate_marketing_costs(self, dates):
        """Simule les coûts marketing"""
        base_marketing = self.config["revenue_base"] * 1000 * 0.10  # 10% des revenus pour le marketing
        
        marketing_costs = []
        for i, date in enumerate(dates):
            growth = 1 + 0.12 * i
            noise = np.random.normal(1, 0.11)
            marketing_costs.append(base_marketing * growth * noise)
        
        return marketing_costs
    
    def _simulate_staff_costs(self, dates):
        """Simule les coûts de personnel"""
        base_staff = self.config["revenue_base"] * 1000 * 0.20  # 20% des revenus pour le personnel
        
        staff_costs = []
        for i, date in enumerate(dates):
            growth = 1 + 0.10 * i
            noise = np.random.normal(1, 0.06)
            staff_costs.append(base_staff * growth * noise)
        
        return staff_costs
    
    def _simulate_net_profit(self, dates):
        """Simule le profit net"""
        profit = []
        for i, date in enumerate(dates):
            base_profit = self.config["revenue_base"] * 1000 * 0.35  # Marge de 35%
            
            year = date.year
            if year >= 2015:
                improvement = 1 + 0.02 * (year - 2015)  # Amélioration progressive de la marge
            else:
                improvement = 1
            
            noise = np.random.normal(1, 0.12)
            profit.append(base_profit * improvement * noise)
        
        return profit
    
    def _simulate_profit_margin(self, dates):
        """Simule la marge de profit"""
        margins = []
        for i, date in enumerate(dates):
            base_margin = 0.35  # Marge initiale de 35%
            
            year = date.year
            if year >= 2015:
                improvement = 1 + 0.01 * (year - 2015)  # Amélioration progressive
            else:
                improvement = 1
            
            noise = np.random.normal(1, 0.05)
            margins.append(base_margin * improvement * noise)
        
        return margins
    
    def _simulate_cac(self, dates):
        """Simule le coût d'acquisition utilisateur"""
        cac_values = []
        for i, date in enumerate(dates):
            base_cac = 5.0  # Coût initial d'acquisition
            
            year = date.year
            if year >= 2015:
                increase = 1 + 0.03 * (year - 2015)  # Augmentation progressive du CAC
            else:
                increase = 1
            
            noise = np.random.normal(1, 0.08)
            cac_values.append(base_cac * increase * noise)
        
        return cac_values
    
    def _simulate_lifetime_value(self, dates):
        """Simule la valeur vie utilisateur"""
        ltv_values = []
        for i, date in enumerate(dates):
            base_ltv = 50.0  # Valeur initiale
            
            year = date.year
            if year >= 2015:
                increase = 1 + 0.05 * (year - 2015)  # Augmentation progressive de la LTV
            else:
                increase = 1
            
            noise = np.random.normal(1, 0.07)
            ltv_values.append(base_ltv * increase * noise)
        
        return ltv_values
    
    def _simulate_ai_investment(self, dates):
        """Simule l'investissement en IA"""
        base_investment = self.config["revenue_base"] * 1000 * 0.08
        
        # Ajustement selon les spécialités
        multiplier = 1.5 if "ai" in self.config["specialites"] else 1.0
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2014, 2018, 2021, 2024]:
                year_multiplier = 1.8  # Pics d'investissement
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.25 * i
            noise = np.random.normal(1, 0.15)
            investment.append(base_investment * growth * year_multiplier * multiplier * noise)
        
        return investment
    
    def _simulate_vr_investment(self, dates):
        """Simule l'investissement en réalité virtuelle"""
        base_investment = self.config["revenue_base"] * 1000 * 0.05
        
        # Ajustement selon les spécialités
        multiplier = 2.0 if "vr" in self.config["specialites"] else 0.8
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2016, 2020, 2023]:
                year_multiplier = 2.0
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.20 * i
            noise = np.random.normal(1, 0.18)
            investment.append(base_investment * growth * year_multiplier * multiplier * noise)
        
        return investment
    
    def _simulate_security_investment(self, dates):
        """Simule l'investissement en sécurité"""
        base_investment = self.config["revenue_base"] * 1000 * 0.04
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2018, 2019, 2021, 2023]:
                year_multiplier = 1.7  # Augmentation après les scandales de sécurité
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.15 * i
            noise = np.random.normal(1, 0.12)
            investment.append(base_investment * growth * year_multiplier * noise)
        
        return investment
    
    def _simulate_growth_investment(self, dates):
        """Simule l'investissement en croissance"""
        base_investment = self.config["revenue_base"] * 1000 * 0.07
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2012, 2014, 2017, 2020, 2023]:
                year_multiplier = 1.6
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.18 * i
            noise = np.random.normal(1, 0.14)
            investment.append(base_investment * growth * year_multiplier * noise)
        
        return investment
    
    def _simulate_content_investment(self, dates):
        """Simule l'investissement en contenu"""
        base_investment = self.config["revenue_base"] * 1000 * 0.06
        
        # Ajustement selon les spécialités
        multiplier = 1.4 if "content" in self.config["specialites"] else 1.0
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            if year in [2015, 2018, 2021, 2024]:
                year_multiplier = 1.5
            else:
                year_multiplier = 1.0
            
            growth = 1 + 0.16 * i
            noise = np.random.normal(1, 0.13)
            investment.append(base_investment * growth * year_multiplier * multiplier * noise)
        
        return investment
    
    def _add_platform_trends(self, df):
        """Ajoute des tendances réalistes adaptées aux plateformes Meta"""
        for i, row in df.iterrows():
            year = row['Annee']
            
            # Croissance initiale (2010-2012)
            if 2010 <= year <= 2012:
                df.loc[i, 'Revenus_Totaux'] *= 1.2
                df.loc[i, 'Utilisateurs_Actifs'] *= 1.15
            
            # Introduction en bourse (2012)
            if year == 2012:
                df.loc[i, 'Revenus_Totaux'] *= 1.25
                df.loc[i, 'Investissement_Croissance'] *= 1.5
            
            # Acquisition d'Instagram (2012) et WhatsApp (2014)
            if year == 2013:
                df.loc[i, 'Utilisateurs_Actifs'] *= 1.1
            if year == 2015:
                df.loc[i, 'Utilisateurs_Actifs'] *= 1.15
            
            # Scandale Cambridge Analytica (2018)
            if year == 2018:
                df.loc[i, 'Utilisateurs_Actifs'] *= 0.97
                df.loc[i, 'Investissement_Securite'] *= 1.8
            
            # Pandémie COVID-19 (2020)
            if year == 2020:
                df.loc[i, 'Utilisateurs_Actifs'] *= 1.12
                df.loc[i, 'Utilisateurs_Quotidiens'] *= 1.15
                df.loc[i, 'Revenus_Publicite'] *= 0.92
            
            # Changement de nom en Meta (2021)
            if year == 2021:
                df.loc[i, 'Investissement_VR'] *= 1.5
                df.loc[i, 'Investissement_IA'] *= 1.3
            
            # Défis réglementaires (2022-2023)
            if 2022 <= year <= 2023:
                df.loc[i, 'Depenses_Totales'] *= 1.1
                df.loc[i, 'Investissement_Securite'] *= 1.2
    
    def create_financial_analysis(self, df):
        """Crée une analyse complète des finances de la plateforme"""
        plt.style.use('seaborn-v0_8')
        fig = plt.figure(figsize=(20, 24))
        
        # 1. Évolution des revenus et dépenses
        ax1 = plt.subplot(4, 2, 1)
        self._plot_revenue_expenses(df, ax1)
        
        # 2. Structure des revenus
        ax2 = plt.subplot(4, 2, 2)
        self._plot_revenue_structure(df, ax2)
        
        # 3. Structure des dépenses
        ax3 = plt.subplot(4, 2, 3)
        self._plot_expenses_structure(df, ax3)
        
        # 4. Investissements stratégiques
        ax4 = plt.subplot(4, 2, 4)
        self._plot_investments(df, ax4)
        
        # 5. Utilisateurs et engagement
        ax5 = plt.subplot(4, 2, 5)
        self._plot_users_engagement(df, ax5)
        
        # 6. Indicateurs de performance
        ax6 = plt.subplot(4, 2, 6)
        self._plot_performance_indicators(df, ax6)
        
        # 7. Profitabilité
        ax7 = plt.subplot(4, 2, 7)
        self._plot_profitability(df, ax7)
        
        # 8. Investissements sectoriels
        ax8 = plt.subplot(4, 2, 8)
        self._plot_sectorial_investments(df, ax8)
        
        plt.suptitle(f'Analyse Financière de {self.platform} - Meta ({self.start_year}-{self.end_year})', 
                    fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(f'{self.platform}_financial_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Générer les insights
        self._generate_financial_insights(df)
    
    def _plot_revenue_expenses(self, df, ax):
        """Plot de l'évolution des revenus et dépenses"""
        ax.plot(df['Annee'], df['Revenus_Totaux'], label='Revenus Totaux', 
               linewidth=2, color='#1877F2', alpha=0.8)
        ax.plot(df['Annee'], df['Depenses_Totales'], label='Dépenses Totales', 
               linewidth=2, color='#E4405F', alpha=0.8)
        
        ax.set_title('Évolution des Revenus et Dépenses (M$)', 
                    fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M$)')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_revenue_structure(self, df, ax):
        """Plot de la structure des revenus"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Revenus_Publicite', 'Revenus_Autres']
        colors = ['#1877F2', '#25D366']
        labels = ['Revenus Publicitaires', 'Autres Revenus']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Structure des Revenus (M$)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M$)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _plot_expenses_structure(self, df, ax):
        """Plot de la structure des dépenses"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Infrastructure', 'R_D', 'Marketing', 'Personnel']
        colors = ['#1877F2', '#25D366', '#E4405F', '#F9A602']
        labels = ['Infrastructure', 'R&D', 'Marketing', 'Personnel']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Structure des Dépenses (M$)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M$)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _plot_investments(self, df, ax):
        """Plot des investissements stratégiques"""
        ax.plot(df['Annee'], df['Investissement_IA'], label='Intelligence Artificielle', 
               linewidth=2, color='#1877F2', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_VR'], label='Réalité Virtuelle', 
               linewidth=2, color='#25D366', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Securite'], label='Sécurité', 
               linewidth=2, color='#E4405F', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Croissance'], label='Croissance', 
               linewidth=2, color='#F9A602', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Contenu'], label='Contenu', 
               linewidth=2, color='#6A0572', alpha=0.8)
        
        ax.set_title('Répartition des Investissements Stratégiques (M$)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M$)')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_users_engagement(self, df, ax):
        """Plot des utilisateurs et engagement"""
        ax.plot(df['Annee'], df['Utilisateurs_Actifs'], label='Utilisateurs Actifs', 
               linewidth=2, color='#1877F2', alpha=0.8)
        
        ax.set_title('Utilisateurs et Engagement', fontsize=12, fontweight='bold')
        ax.set_ylabel('Utilisateurs Actifs', color='#1877F2')
        ax.tick_params(axis='y', labelcolor='#1877F2')
        ax.grid(True, alpha=0.3)
        
        # Utilisateurs quotidiens en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Utilisateurs_Quotidiens'], label='Utilisateurs Quotidiens', 
                linewidth=2, color='#25D366', alpha=0.8)
        ax2.set_ylabel('Utilisateurs Quotidiens', color='#25D366')
        ax2.tick_params(axis='y', labelcolor='#25D366')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_performance_indicators(self, df, ax):
        """Plot des indicateurs de performance"""
        # Coût d'acquisition utilisateur
        ax.plot(df['Annee'], df['Cout_Acquisition_Utilisateur'], label='Coût d\'Acquisition (CAC)', 
               linewidth=2, color='#E4405F', alpha=0.8)
        
        ax.set_title('Indicateurs de Performance', fontsize=12, fontweight='bold')
        ax.set_ylabel('Coût d\'Acquisition (CAC)', color='#E4405F')
        ax.tick_params(axis='y', labelcolor='#E4405F')
        ax.grid(True, alpha=0.3)
        
        # Valeur vie utilisateur en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Vie_Utilisateur'], label='Valeur Vie Utilisateur (LTV)', 
                linewidth=2, color='#1877F2', alpha=0.8)
        ax2.set_ylabel('Valeur Vie Utilisateur (LTV)', color='#1877F2')
        ax2.tick_params(axis='y', labelcolor='#1877F2')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_profitability(self, df, ax):
        """Plot de la profitabilité"""
        # Profit net
        ax.bar(df['Annee'], df['Profit_Net'], label='Profit Net (M$)', 
              color='#25D366', alpha=0.7)
        
        ax.set_title('Profitabilité', fontsize=12, fontweight='bold')
        ax.set_ylabel('Profit Net (M$)', color='#25D366')
        ax.tick_params(axis='y', labelcolor='#25D366')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Marge de profit en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Marge_Profit'], label='Marge de Profit', 
                linewidth=3, color='#1877F2')
        ax2.set_ylabel('Marge de Profit', color='#1877F2')
        ax2.tick_params(axis='y', labelcolor='#1877F2')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_sectorial_investments(self, df, ax):
        """Plot des investissements sectoriels"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Investissement_IA', 'Investissement_VR', 
                     'Investissement_Securite', 'Investissement_Croissance', 
                     'Investissement_Contenu']
        
        colors = ['#1877F2', '#25D366', '#E4405F', '#F9A602', '#6A0572']
        labels = ['IA', 'RV', 'Sécurité', 'Croissance', 'Contenu']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Répartition Sectorielle des Investissements (M$)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M$)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _generate_financial_insights(self, df):
        """Génère des insights analytiques adaptés aux plateformes Meta"""
        print(f"📊 INSIGHTS ANALYTIQUES - {self.platform} (Meta)")
        print("=" * 60)
        
        # 1. Statistiques de base
        print("\n1. 📈 STATISTIQUES GÉNÉRALES:")
        avg_revenue = df['Revenus_Totaux'].mean()
        avg_expenses = df['Depenses_Totales'].mean()
        avg_profit = df['Profit_Net'].mean()
        avg_users = df['Utilisateurs_Actifs'].mean()
        
        print(f"Revenus moyens annuels: {avg_revenue:.2f} M$")
        print(f"Dépenses moyennes annuelles: {avg_expenses:.2f} M$")
        print(f"Profit net moyen: {avg_profit:.2f} M$")
        print(f"Utilisateurs actifs moyens: {avg_users/1000000:.2f} M")
        
        # 2. Croissance
        print("\n2. 📊 TAUX DE CROISSANCE:")
        revenue_growth = ((df['Revenus_Totaux'].iloc[-1] / 
                          df['Revenus_Totaux'].iloc[0]) - 1) * 100
        user_growth = ((df['Utilisateurs_Actifs'].iloc[-1] / 
                       df['Utilisateurs_Actifs'].iloc[0]) - 1) * 100
        
        print(f"Croissance des revenus ({self.start_year}-{self.end_year}): {revenue_growth:.1f}%")
        print(f"Croissance des utilisateurs ({self.start_year}-{self.end_year}): {user_growth:.1f}%")
        
        # 3. Structure financière
        print("\n3. 📋 STRUCTURE FINANCIÈRE:")
        ad_share = (df['Revenus_Publicite'].mean() / df['Revenus_Totaux'].mean()) * 100
        randd_share = (df['R_D'].mean() / df['Depenses_Totales'].mean()) * 100
        infra_share = (df['Infrastructure'].mean() / df['Depenses_Totales'].mean()) * 100
        
        print(f"Part de la publicité dans les revenus: {ad_share:.1f}%")
        print(f"Part de la R&D dans les dépenses: {randd_share:.1f}%")
        print(f"Part de l'infrastructure dans les dépenses: {infra_share:.1f}%")
        
        # 4. Performance
        print("\n4. 💰 INDICATEURS DE PERFORMANCE:")
        avg_profit_margin = df['Marge_Profit'].mean() * 100
        avg_cac = df['Cout_Acquisition_Utilisateur'].mean()
        avg_ltv = df['Vie_Utilisateur'].mean()
        ltv_cac_ratio = avg_ltv / avg_cac
        
        print(f"Marge de profit moyenne: {avg_profit_margin:.1f}%")
        print(f"Coût d'acquisition utilisateur moyen: {avg_cac:.2f} $")
        print(f"Valeur vie utilisateur moyenne: {avg_ltv:.2f} $")
        print(f"Ratio LTV/CAC: {ltv_cac_ratio:.2f}")
        
        # 5. Spécificités de la plateforme
        print(f"\n5. 🌟 SPÉCIFICITÉS DE {self.platform.upper()}:")
        print(f"Type de plateforme: {self.config['type']}")
        print(f"Spécialités: {', '.join(self.config['specialites'])}")
        
        # 6. Événements marquants
        print("\n6. 📅 ÉVÉNEMENTS MARQUANTS:")
        print("• 2012: Introduction en bourse de Facebook")
        print("• 2012-2014: Acquisitions d'Instagram et WhatsApp")
        print("• 2018: Scandale Cambridge Analytica et renforcement de la sécurité")
        print("• 2020: Pandémie COVID-19 - augmentation de l'utilisation")
        print("• 2021: Changement de nom en Meta et accent sur le métavers")
        print("• 2022-2023: Défis réglementaires et concurrence accrue")
        
        # 7. Recommandations stratégiques
        print("\n7. 💡 RECOMMANDATIONS STRATÉGIQUES:")
        if self.platform == "Facebook":
            print("• Diversifier les sources de revenus au-delà de la publicité")
            print("• Améliorer l'engagement des jeunes utilisateurs")
            print("• Développer les fonctionnalités de commerce électronique")
        elif self.platform == "Instagram":
            print("• Contrer la concurrence de TikTok avec des fonctionnalités innovantes")
            print("• Développer les outils pour créateurs de contenu")
            print("• Améliorer la monétisation des Reels")
        elif self.platform == "WhatsApp":
            print("• Accélérer la monétisation via les API business")
            print("• Développer les services financiers et de paiement")
            print("• Améliorer l'intégration avec les autres plateformes Meta")
        
        print("• Investir dans l'IA générative pour améliorer l'expérience utilisateur")
        print("• Développer la réalité augmentée/virtuelle pour le métavers")
        print("• Renforcer la protection des données et la confidentialité")
        print("• Explorer de nouveaux marchés émergents")

def main():
    """Fonction principale pour Meta"""
    # Liste des plateformes Meta
    platforms = ["Facebook", "WhatsApp", "Instagram"]
    
    print("📊 ANALYSE FINANCIÈRE DES PLATEFORMES META (2010-2025)")
    print("=" * 60)
    
    # Demander à l'utilisateur de choisir une plateforme
    print("Plateformes disponibles:")
    for i, platform in enumerate(platforms, 1):
        print(f"{i}. {platform}")
    
    try:
        choix = int(input("\nChoisissez le numéro de la plateforme à analyser: "))
        if choix < 1 or choix > len(platforms):
            raise ValueError
        platform_selectionnee = platforms[choix-1]
    except (ValueError, IndexError):
        print("Choix invalide. Sélection de Facebook par défaut.")
        platform_selectionnee = "Facebook"
    
    # Initialiser l'analyseur
    analyzer = MetaFinanceAnalyzer(platform_selectionnee)
    
    # Générer les données
    financial_data = analyzer.generate_financial_data()
    
    # Sauvegarder les données
    output_file = f'{platform_selectionnee}_financial_data_2010_2025.csv'
    financial_data.to_csv(output_file, index=False)
    print(f"💾 Données sauvegardées: {output_file}")
    
    # Aperçu des données
    print("\n👀 Aperçu des données:")
    print(financial_data[['Annee', 'Utilisateurs_Actifs', 'Revenus_Totaux', 'Depenses_Totales', 'Profit_Net']].head())
    
    # Créer l'analyse
    print("\n📈 Création de l'analyse financière...")
    analyzer.create_financial_analysis(financial_data)
    
    print(f"\n✅ Analyse financière de {platform_selectionnee} terminée!")
    print(f"📊 Période: {analyzer.start_year}-{analyzer.end_year}")
    print("📦 Données: Utilisateurs, revenus, dépenses, investissements")

if __name__ == "__main__":
    main()