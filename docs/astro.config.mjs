// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

export default defineConfig({
	site: 'https://alibby-python.github.io',

	// Remove when custom domain is enabled.
	base: '/create-react-app',

	integrations: [
		starlight({
			title: "Create Python App",
			logo: {
				src: './src/assets/cpa-logo.png',
				alt: 'Create Python App',
				replacesTitle: true,
			},

			customCss: [
				'./src/styles/custom.css'
			],			
			description:
				"Documentation for Create Python App.",
			head: [
				{
					tag: "link",
					attrs: {
						rel: "icon",
						type: "image/png",
						href: "/favicon.png"
					},
				},
			],
			social: [
				{
					icon: "github",
					label: "GitHub",
					href: "https://github.com/alibby-python/create-python-app",
				},
			],

			sidebar: [
				{
					label: "Getting Started",
					items: [
						{
							label: "Installation",
							slug: "getting-started/installation",
						},
						{
							label: "Quick Start",
							slug: "getting-started/quick-start",
						},
					],
				},

				{
					label: "Guides",
					items: [
						{
							autogenerate: {
								directory: "guides",
							},
						},
					],
				},

				{
					label: "Reference",
					items: [
						{
							autogenerate: {
								directory: "reference",
							},
						},
					],
				},

				{
					label: "Contributing",
					items: [
						{
							label: "Contributing",
							slug: "contributing",
						},
					],
				},
			],
		}),
	],
});